"use client"

import { useState } from "react";
import { signIn } from "next-auth/react";
import { useRouter } from "next/navigation";


export default function LoginPage() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const router = useRouter();

    const handleLogin = async (e) => {
        e.preventDefault();
        setError("");

        try {
            const result = await signIn("credentials", {
                email, password, redirect: false
            });
            router.push("/protected");
        } catch(err) {
            setError("로그인 실패. 다시 시도해주세요.");
        }
    }

    return (
        <div>
            <h2>로그인</h2>
            <form onSubmit = {handleLogin}>
                <div><input type="email" placeholder="email@example.com" value={email} onChange={(e)=>
                    setEmail(e.target.value)}/></div>
                <div><input type="password" placeholder="password" value={password} onChange={(e)=>
                    setPassword(e.target.value)}/></div>
                <div><input type="submit" value="login"></input></div>
            </form>
            {error && <p style={{ color: "red"}}>{error}</p>}
        </div>
    );
}