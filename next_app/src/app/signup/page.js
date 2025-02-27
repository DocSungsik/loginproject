"use client"

import { useState } from "react";

import axios from "axios";

export default function SignupPage(){
    const [id, setId] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");
    const [phone, setPhone] = useState("");

    const handleSignup = async (e) => {
        try{
            const response = await axios.post(process.env.NEXT_PUBLIC_API_URL + "signup", {id: id, password: password, email: email, phone: phone});
            alert("Signup successful");
        } catch(err) {
            alert("Signup again");
        }
    }

    return (
        <div>
            <h2>Signup</h2>
            <form onSubmit={handleSignup}>
                <div><input type="email" placeholder="email@example.com" value={email} onChange={(e)=>
                    setEmail(e.target.value)}/></div>
                <div><input type="password" placeholder="password" value={password} onChange={(e)=>
                    setPassword(e.target.value)}/></div>
                <div><input type="text" name="name" placeholder="name" value={id} onChange={(e)=>
                    setId(e.target.value)}/></div>
                <div><input type="text" name="phone" placeholder="000-0000-0000" value={phone} onChange={(e)=>
                    setPhone(e.target.value)}/></div>
                <div><input type="submit" value = "signup"></input></div>
            </form>
        </div>
    )
}
