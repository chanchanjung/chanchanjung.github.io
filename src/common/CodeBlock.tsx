import SyntaxHighlighter from 'react-syntax-highlighter';
import { docco } from 'react-syntax-highlighter/dist/esm/styles/hljs';
export const CodeBlock = () => {
    const codeString = '(num) => num + 1';
    return (
        <SyntaxHighlighter language="" style={docco}>
            {codeString}
        </SyntaxHighlighter>
    );
};

// import React, { PureComponent } from "react";
// import PropTypes from "prop-types";
//
// class CodeBlock extends PureComponent {
//     static propTypes = {
//         value: PropTypes.string.isRequired,
//         language: PropTypes.string
//     };
//
//     static defaultProps = {
//         language: null
//     };
//
//     render() {
//         const { language, value } = this.props;
//         return (
//             <SyntaxHighlighter language={language} style={docco}>
//                 {value}
//             </SyntaxHighlighter>
//         );
//     }
// }
//
// export default CodeBlock;