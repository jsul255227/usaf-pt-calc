import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Helmet } from "react-helmet";

function getPalette(isDark) {
  return isDark
    ? {
        bg: "#101624",
        card: "#181f2e",
        cardShadow: "0 2px 16px 0 rgba(0,0,0,0.32)",
        text: "#e3e8f0",
        accent: "#7bb0ff",
        inputBg: "#181f2e",
        inputText: "#e3e8f0",
        inputBorder: "#3a4660",
        label: "#b3c6e0",
        resultLabel: "#7bb0ff",
        error: "#ff6b6b",
        warning: "#ffd166",
        buttonBg: "#223366",
        buttonText: "#fff",
        menuBg: "#181f2e",
      }
    : {
        bg: "#f8fafc",
        card: "#fff",
        cardShadow: "0 2px 16px 0 rgba(0,0,0,0.08)",
        text: "#003366",
        accent: "#174ea6",
        inputBg: "#fff",
        inputText: "#003366",
        inputBorder: "#b0b8c1",
        label: "#003366",
        resultLabel: "#174ea6",
        error: "#b00020",
        warning: "#b08000",
        buttonBg: "#003366",
        buttonText: "#fff",
        menuBg: "#fff",
      };
}

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

export default function Contact({ darkMode }) {
  // Mobile detection
  const [isMobile, setIsMobile] = useState(
    typeof window !== 'undefined' && window.matchMedia('(max-width: 600px)').matches
  );
  useEffect(() => {
    const mq = window.matchMedia('(max-width: 600px)');
    const handler = (e) => setIsMobile(e.matches);
    mq.addEventListener('change', handler);
    return () => mq.removeEventListener('change', handler);
  }, []);

  const palette = getPalette(darkMode);
  const contactStyle = {
    maxWidth: 480,
    width: '100%',
    margin: isMobile ? '0' : '2rem auto',
    padding: isMobile ? 0 : 24,
    background: palette.card, // use palette.card for background
    borderRadius: isMobile ? 0 : 16,
    boxShadow: isMobile ? 'none' : palette.cardShadow,
    fontFamily: "Inter, system-ui, Arial, sans-serif",
    color: palette.text,
    minHeight: isMobile ? '100vh' : undefined,
    transition: 'background 0.3s',
  };
  const headingStyle = {
    fontSize: 28,
    fontWeight: 700,
    marginBottom: 24,
    letterSpacing: 1,
    textAlign: "center",
    borderBottom: `2px solid ${darkMode ? '#223366' : '#e0e6ed'}`,
    paddingBottom: 12,
    color: palette.text,
  };
  const navigate = useNavigate();
  return (
    <>
      <Helmet>
        <title>USAF PT Calculator – Contact</title>
        <meta name="description" content="Contact the USAF PT Calculator team for support, feedback, or legal inquiries." />
        <meta property="og:title" content="USAF PT Calculator – Contact" />
        <meta property="og:description" content="Contact the USAF PT Calculator team for support, feedback, or legal inquiries." />
        <meta property="og:type" content="article" />
      </Helmet>
      <div style={{
        minHeight: "100vh",
        background: palette.bg, // always use palette.bg for outer background
        transition: "background 0.3s",
      }}>
        <div style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "flex-start",
          minHeight: "100vh",
          padding: isMobile ? 0 : "48px 0",
          background: palette.bg, // ensure palette.bg is used here too
          transition: "background 0.3s",
        }}>
          <div style={contactStyle}>
            <button
              onClick={() => navigate("/")}
              style={{
                position: "fixed",
                top: 24,
                right: 24,
                zIndex: 2100,
                background: palette.accent,
                color: palette.buttonText,
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
              <a href="mailto:usafptcalc@protonmail.com" style={{ color: palette.accent, textDecoration: "underline" }}>
                usafptcalc@protonmail.com
              </a>
            </div>
            <div style={{ fontSize: 15, color: darkMode ? '#b3c6e0' : '#555' }}>
              © 2025 USAF PT Calc. All rights reserved.<br />
              This site is not endorsed by the U.S. Air Force.
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
