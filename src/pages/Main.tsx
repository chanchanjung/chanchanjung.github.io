import {Col, Container, Row} from "../common/Container";
import {Button} from "../common/Button";
import {MarkdownRenderer} from "../common/MarkdownRenderer";
import {useNavigate} from "react-router-dom";


export function Main() {
    const navigate = useNavigate();
    return (
        <Container style={{backgroundColor: "black", height: "100vh"}}>
            <Row className="d-flex justify-content-center align-items-center">
                <Col/>
                <Col colSpan={3} style={{color: "white"}}>
                    <div>
                        <Button>Algorithm</Button>
                        <Button onClick={() => navigate("/interface")} >Java</Button>
                    </div>
                </Col>
                <Col/>
            </Row>
        </Container>
    );
}