import React, { Component } from "react";
import styled from "styled-components";

import posed, { PoseGroup } from "react-pose";

let _defaultDiff = 12;
let _defaultWidth = 90;
let _defaultMin = 5;

const Navbar = styled.div`
  box-sizing: border-box;
  background: #ccc;
  padding: 15px;
  width: 100%;
  display: flex;
  justify-content: space-between;

  > * {
    display: flex;
  }
`;

const Container = styled.div`
  display: flex;
  position: relative;
  justify-content: center;
  padding: 2em;
  background: #ff0000;
  height: calc(100vh - 60px);
`;

const Card = styled.div`
  position: absolute;
  height: 600px;
  background-color: rgba(255, 255, 255, 0.2);
  border: 2px solid rgba(255, 255, 255, 1);
  border-radius: 1rem;
  padding: 1em;
  box-sizing: border-box;
  margin: 0 auto;

  &:nth-last-child(4) {
    top: ${_defaultDiff * 2}px;
    width: ${_defaultWidth - _defaultMin * 3}%;
    background-color: rgba(255, 255, 255, 0.4);
  }
  &:nth-last-child(3) {
    top: ${_defaultDiff * 3}px;
    width: ${_defaultWidth - _defaultMin * 2}%;
    background-color: rgba(255, 255, 255, 0.6);
  }
  &:nth-last-child(2) {
    top: ${_defaultDiff * 4}px;
    width: ${_defaultWidth - _defaultMin * 1}%;
    background-color: rgba(255, 255, 255, 0.8);
  }

  &:nth-last-child(1) {
    top: ${_defaultDiff * 5}px;
    width: ${_defaultWidth - _defaultMin * 0}%;
    background-color: rgba(255, 255, 255, 1);
  }
`;

const PosedCard = posed(Card)({
  enter: { opacity: 1 },
  exit: { opacity: 0 }
});

class App extends Component {
  state = {
    currentID: 0,
    cards: [
      { id: "A", color: "#333" },
      { id: "B", color: "#333" },
      { id: "C", color: "#333" },
      { id: "D", color: "#333" },
      { id: "E", color: "#333" },
      { id: "F", color: "#333" },
      { id: "G", color: "#333" }
    ]
  };

  render() {
    return (
      <div className="App">
        <Navbar>
          <button
            onClick={() =>
              this.setState({ currentID: this.state.currentID - 1 })
            }
          >
            Back
          </button>
          <button
            onClick={() =>
              this.setState({ currentID: this.state.currentID + 1 })
            }
          >
            Next
          </button>
        </Navbar>

        <Container>
          <PoseGroup>
            {this.state.cards
              .slice(this.state.currentID, this.state.currentID + 4)
              .reverse()
              .map(card => (
                <PosedCard key={card.id}>Card: {card.id}</PosedCard>
              ))}
          </PoseGroup>
        </Container>
      </div>
    );
  }
}

export default App;
