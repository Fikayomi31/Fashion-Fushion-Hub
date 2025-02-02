import React, { useState, useEffect } from 'react';
import { register } from '../../utils/auth';
import { useNavigate, Link } from 'react-router-dom';
import { useAuthStore } from '../../store/auth';

function Register() {
    const [fullname, setFullname] = useState("");
    const [email, setEmail] = useState("");
    const [mobile, setMobile] = useState("");
    const [password, setPassword] = useState("");
    const [password2, setPassword2] = useState("");
    const [isLoading, setIsLoading] = useState(false);

    const navigate = useNavigate();
    const isLoggedIn = useAuthStore((state) => state.isLoggedIn);

    useEffect(() => {
        if (isLoggedIn && isLoggedIn()) {
            navigate("/");
        }
    }, [isLoggedIn, navigate]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);

        try {
            const { error } = await register(fullname, email, mobile, password, password2);
            if (error) {
                alert(JSON.stringify(error));
            } else {
                navigate("/");
            }
        } catch (err) {
            console.error("Registration error:", err);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <>
            <h1>Register Here</h1>
            <form onSubmit={handleSubmit}>
                <input type='text' placeholder='Full Name' name='full_name' id='full_name' 
                onChange={(e) => setFullname(e.target.value)} required /><br/><br/>

                <input type='email' placeholder='Email' name='email' id='email' 
                onChange={(e) => setEmail(e.target.value)} required /><br/><br/>

                <input type='text' placeholder='Mobile' name='mobile' id='mobile' 
                onChange={(e) => setMobile(e.target.value)} required /><br/><br/>

                <input type='password' placeholder='Password' name='password' id='password' 
                onChange={(e) => setPassword(e.target.value)} required /><br/><br/>

                <input type='password' placeholder='Confirm Password' name='password2' id='password2' 
                onChange={(e) => setPassword2(e.target.value)} required /><br/><br/>

                <button type='submit' disabled={isLoading}>
                    {isLoading ? "Registering..." : "Register"}
                </button>
            </form>
        </>
    );
}

export default Register;
