import Home from "./pages/Home";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./Pages/Login";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/chat" element={<Home />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;