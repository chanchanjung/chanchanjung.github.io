import {useState} from "react";


export const MarkdownRenderer = (markdownPath: string) => {
    const [markdownData, setMarkdownData] = useState('');
    fetch(markdownPath)
        .then(res => res.text())
        .then(res => setMarkdownData(res))
        .catch(err => console.log(err));
    return markdownData;
}