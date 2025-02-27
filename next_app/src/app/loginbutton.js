"use client"
import { useSession } from "next-auth/react"
import Link from 'next/link';

export function LoginButton() {
    const {data: session} = useSession();

    if (!session) {
        return (
            <div>
            <button type="button"><Link href="/login">Login</Link></button>
            <button type="button"><Link href="/signup">Signup</Link></button>
            </div>
        )
    } else {
        return (
            <div>
            <button type="button"><Link href="/logout">Logout</Link></button>
            </div>
        )
    }
}