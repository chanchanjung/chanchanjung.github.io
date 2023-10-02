import styled from "styled-components";

export const Container = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
`

export const Row = styled.div`
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;
`

export const Col = styled.div<{ colSpan?: number }>`
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-basis: 100%;
  flex: 1;
  flex-grow: ${(props) => props.colSpan ?? 1};
`