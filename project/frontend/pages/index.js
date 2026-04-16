import {  useEFFect, useState } from "react";
export default function Home() {
    const [posts, setPosts] = useState([]);

    useEFFect(() => {
        fetch("http://localhost:8000/posts")
            .then(res => res.json())
            .then(data => setPosts(data));
    }, []);

    return (
        <div>
            <h1>ブログ一覧</h1>
            {posts.map((p,i) => (
                <div key={i}>
                    <h2>{p[1]}</h2>
                    <p>{p[2]}</p>
                </div>
            ))}
        </div>
    );
}