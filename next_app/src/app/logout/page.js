"use client"

import { signOut } from "next-auth/react";
import { useRouter } from "next/navigation";

export default function LogoutPage(){
    const router = useRouter();
    return (
        <div>
            <h2>Logout</h2>
            <button onClick={() => {
                signOut({ callbackUrl: '/login'});
            }}>Logout</button>
        </div>
    )
}