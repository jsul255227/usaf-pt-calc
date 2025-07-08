import React from "react";
import { useNavigate } from "react-router-dom";

const contactStyle = {
  maxWidth: 480,
  margin: "2rem auto",
  padding: 24,
  background: "#fff",
  borderRadius: 16,
  boxShadow: "0 2px 16px 0 rgba(0,0,0,0.08)",
  fontFamily: "Inter, system-ui, Arial, sans-serif",
  color: "#003366",
};
const headingStyle = {
  fontSize: 28,
  fontWeight: 700,
  marginBottom: 24,
  letterSpacing: 1,
  textAlign: "center",
  borderBottom: "2px solid #e0e6ed",
  paddingBottom: 12,
};

export default function Contact() {
  const navigate = useNavigate();
  return (
    <div style={contactStyle}>
      <button
        onClick={() => navigate("/")}
        style={{
          position: "fixed",
          top: 24,
          right: 24,
          zIndex: 2100,
          background: "#174ea6",
          color: "#fff",
          border: "none",
          borderRadius: "50%",
          width: 48,
          height: 48,
          fontSize: 28,
          cursor: "pointer",
        }}
        aria-label="Back to main"
      >
        ←
      </button>
      <div style={headingStyle}>Contact</div>
      <div style={{ fontSize: 18, marginBottom: 16 }}>
        For bug reports, suggestions, and feedback, please email us at:
      </div>
      <div style={{ fontSize: 20, fontWeight: 600, marginBottom: 24 }}>
        <a href="mailto:usafptcalc@protonmail.com" style={{ color: "#174ea6", textDecoration: "underline" }}>
          usafptcalc@protonmail.com
        </a>
      </div>
      <div style={{ fontSize: 15, color: "#555" }}>
        © 2025 USAF PT Calc. All rights reserved.<br />
        This site is not endorsed by the U.S. Air Force.
      </div>
    </div>
  );
}
