"use client"

import { useEffect, useState } from "react";
import { SessionProvider, useSession } from "next-auth/react";

export default function ProtectedPage() {
    const { data: session, status } = useSession();

    if (status === "loading") return <p>Loading...</p>;
    if (!session) return <p>Access Denied</p>;

    return (
        <div>
            <h1> Welcome, {session.user?.name || "User"}! </h1>
        </div>
    )
}