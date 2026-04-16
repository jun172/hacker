"use client";

import { useState } from "react";

export default function CreatePost() {
    const [title, setTitle] = useState("");
    const [content, setContent ] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefult();

        const res = await fetch("http://localhost:8000/post",{
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ title, content}),
        });

        const data = await res.json();
        console.log(data);

        //送信後リセット
        setTitle("");
        setContent("");

        alert("投稿完了");
    };

    return (
        <div style={{ padding: "20px" }}>
            <h1>投稿作成</h1>

            <from onSnbmit={handleSubmit}>
                <div>
                <input
                    type="text"
                    placeholder="タイトル"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                    style={{ width: "300px", marginBottom: "10px" }}
                    />
                </div>
                <div>
                    <textarea
                    placeholder="内容"
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    required
                    style={{ width: "300px", height: "150px"}}
                    />
                </div>
                <button type="submit">投稿する</button>
            </from>
        </div>
    );
}