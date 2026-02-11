import hashlib
import streamlit as st
from db import execute_query, execute_query_one
import secrets

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password(password, hashed):
    return hash_password(password) == hashed

def register_user(username, email, password):
    existing = execute_query_one(
        "SELECT user_id FROM users WHERE username = %s OR email = %s",
        (username, email)
    )
    
    if existing:
        return False, "Username or email already exists"
    
    password_hash = hash_password(password)
    user_id = execute_query(
        "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
        (username, email, password_hash)
    )
    
    if user_id:
        return True, "Registration successful"
    return False, "Registration failed"

def login_user(username, password):
    user = execute_query_one(
        "SELECT user_id, username, email, password_hash FROM users WHERE username = %s",
        (username,)
    )
    
    if user and verify_password(password, user['password_hash']):
        return True, user
    return False, None

def logout_user():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

def generate_reset_token():
    """Generate secure reset token"""
    return secrets.token_urlsafe(32)

def request_password_reset(email):
    """Request password reset"""
    user = execute_query_one(
        "SELECT user_id, username FROM users WHERE email = %s",
        (email,)
    )
    
    if not user:
        return False, "Email not found"
    
    reset_token = generate_reset_token()
    
    # Store token in database (add reset_token column to users table)
    execute_query(
        "UPDATE users SET reset_token = %s WHERE email = %s",
        (reset_token, email)
    )
    
    return True, f"Reset code: {reset_token[:8]}"

def reset_password(reset_code, new_password):
    """Reset password using token"""
    user = execute_query_one(
        "SELECT user_id FROM users WHERE reset_token LIKE %s",
        (reset_code + '%',)
    )
    
    if not user:
        return False, "Invalid reset code"
    
    password_hash = hash_password(new_password)
    execute_query(
        "UPDATE users SET password_hash = %s, reset_token = NULL WHERE user_id = %s",
        (password_hash, user['user_id'])
    )
    
    return True, "Password reset successful"