import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

const App = () => {
  const [country, setCountry] = useState(null);
  const [capitalGuess, setCapitalGuess] = useState("");
  const [result, setResult] = useState("");
  const [uuid, setUuid] = useState("");

  const fetchCountry = async () => {
    try {
      const response = await axios.get(
        "http://localhost:8000/api/v1/countries_and_capitals/"
      );
      const data = response.data.payload;

      setCountry(data.country);
      setUuid(data.uuid);
    } catch (error) {
      console.log(error);
    }
  };

  const checkCorrectGuess = async () => {
    try {
      const response = await axios.post(
        "http://localhost:8000/api/v1/countries_and_capitals/",
        { uuid: uuid, capital: capitalGuess }
      );
      const capital = response.data.payload;

      if (response.data.success) {
        setResult("Congratulations! Your guess is correct.");
      } else {
        setResult(`Incorrect guess. The correct capital is ${capital}.`);
      }

      setTimeout(() => {
        fetchCountry();
        setCapitalGuess("");
        setResult("");
      }, 2000);
    } catch (error) {
      console.log(error);
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    checkCorrectGuess();
  };

  useEffect(() => {
    fetchCountry();
  }, []);

  return (
    <div className="container">
      <h1 className="title">Capital Guessing Game</h1>
      {country && (
        <div className="guess-form">
          <h2 className="country-title">Guess the capital of {country}:</h2>
          <form onSubmit={handleSubmit}>
            <input
              className="input-field"
              type="text"
              value={capitalGuess}
              onChange={(event) => setCapitalGuess(event.target.value)}
              required
            />
            <button className="submit-btn" type="submit">
              Check
            </button>
          </form>
        </div>
      )}
      {result && (
        <div className="result">
          <p className="result-message">{result}</p>
        </div>
      )}
    </div>
  );
};

export default App;
