import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../services/authService";



function LoginForm() {
    const navigate = useNavigate();
  const [rollNumber, setRollNumber] = useState("");
  const [password, setPassword] = useState("");

 const handleLogin = async () => {
  try {
    const data = await login({
      roll_number: rollNumber,
      password: password,
    });

    console.log(data);

    localStorage.setItem("student_id", data.student_id);
    localStorage.setItem("student_name", data.full_name);

    navigate("/chat");

  } catch (error) {
    alert(error.message);
  }
};

  return (
    <div className="card p-4 mx-auto" style={{ maxWidth: "400px" }}>
      <div className="mb-3">
        <label>Roll Number</label>
        <input
          className="form-control"
          value={rollNumber}
          onChange={(e) => setRollNumber(e.target.value)}
        />
      </div>

      <div className="mb-3">
        <label>Password</label>
        <input
          type="password"
          className="form-control"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>

      <button
        className="btn btn-primary"
        onClick={handleLogin}
      >
        Login
      </button>
    </div>
  );
}

export default LoginForm;