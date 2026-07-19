function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg bg-light border-bottom px-4">
      <div className="container-fluid">

        {/* Logo / Title */}
        <span className="navbar-brand fw-bold">
          🎓 Student Chatbot
        </span>

        {/* Right Side */}
        <div className="d-flex align-items-center gap-3">

          <button className="btn btn-primary">
            + New Chat
          </button>

          <div
            className="rounded-circle bg-secondary text-white d-flex justify-content-center align-items-center"
            style={{
              width: "40px",
              height: "40px",
            }}
          >
            A
          </div>

        </div>

      </div>
    </nav>
  );
}

export default Navbar;