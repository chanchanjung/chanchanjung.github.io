import {MarkdownRenderer} from "../../common/MarkdownRenderer";
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";
import MARKDOWN from "posts/java/Interface.md";
import rehypeRaw from "rehype-raw";
import SyntaxHighlighter, {PrismLight} from "react-syntax-highlighter";
import {materialDark, materialLight} from "react-syntax-highlighter/dist/cjs/styles/prism";
import {Col, Container, Row} from "../../common/Container";

export const Interface = () => {
    const markdownData = MarkdownRenderer(MARKDOWN);
    return(
        <Container>
            <Row>
                <Col/>
                <Col/>
                <Col
                    colSpan={3}
                >
                    <Markdown
                        remarkPlugins={[remarkGfm]}
                        rehypePlugins={[rehypeRaw]}
                        components={{
                            code({ node, inline, className, children, ...props }) {
                                const match = /language-(\w+)/.exec(className || "");
                                return !inline && match ? (
                                    <SyntaxHighlighter
                                        style={materialDark}
                                        customStyle={{width: "70vh"}}
                                        PreTag="div"
                                        language={match[1]}
                                        children={String(children).replace(/\n$/, "")}
                                        {...props}
                                    />
                                ) : (
                                    <code style={{width: "50vh"}} className={className ? className : ""} {...props}>
                                        {children}
                                    </code>
                                );
                            }
                        }}
                    >{markdownData}</Markdown>
                </Col>
                <Col/>
                <Col/>

            </Row>

        </Container>
    )
}