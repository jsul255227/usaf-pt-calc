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

const faqStyle = {
  maxWidth: 600,
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
const sectionStyle = {
  margin: "24px 0",
  borderTop: "1px solid #e0e6ed",
  paddingTop: 18,
};
const qStyle = { fontWeight: 600, marginBottom: 6 };
const aStyle = { marginBottom: 12 };

export default function FAQ({ darkMode }) {
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
  const faqStyle = {
    maxWidth: 600,
    width: '100%',
    margin: isMobile ? '0' : '2rem auto',
    padding: isMobile ? 0 : 24,
    background: palette.card, // use palette.card instead of palette.bg or '#fff'
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
  const sectionStyle = {
    margin: "24px 0",
    borderTop: `1px solid ${darkMode ? '#223366' : '#e0e6ed'}`,
    paddingTop: 18,
  };
  const qStyle = { fontWeight: 600, marginBottom: 6, color: palette.label };
  const aStyle = { marginBottom: 12 };
  const navigate = useNavigate();
  return (
    <>
      <Helmet>
        <title>USAF PT Calculator – FAQ</title>
        <meta name="description" content="Answers to common questions about the Air Force PT test and this calculator. Learn about scoring, requirements, and more." />
        <meta property="og:title" content="USAF PT Calculator – FAQ" />
        <meta property="og:description" content="Answers to common questions about the Air Force PT test and this calculator." />
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
          <div style={faqStyle}>
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
            <div style={headingStyle}>USAF PT Calc – FAQ</div>
            <div style={sectionStyle}>
              <div style={qStyle}>1. What Does the Air Force PT Test Include?</div>
              <div style={aStyle}>
                Cardio: 1.5-mile run (or a medically approved alternative) — up to 60
                points.
                <br />
                Muscular Strength: Push-ups (standard or hand-release) — up to 20
                points.
                <br />
                Core Endurance: Sit-ups, cross-leg reverse crunches, or forearm plank —
                up to 20 points.
                <br />
                <br />
                <b>Total Score: 100 points</b>
              </div>
            </div>
            <div style={sectionStyle}>
              <div style={qStyle}>2. How Does Scoring Work with Updated Age Groups?</div>
              <div style={aStyle}>
                Scoring is based on five-year age brackets for fair evaluation.
                <br />
                Standards vary by age and gender.
                <br />
                The app automatically applies relevant standards based on your profile.
              </div>
            </div>
            <div style={sectionStyle}>
              <div style={qStyle}>3. What Qualifies as Passing the PT Test?</div>
              <div style={aStyle}>
                To pass:
                <br />
                Achieve a composite score of 75 or higher.
                <br />
                Meet/exceed minimum standards for each component.
                <br />
                <br />
                <i>
                  Note: Failing any one component results in failing the entire test,
                  regardless of the total score.
                </i>
              </div>
            </div>
            <div style={sectionStyle}>
              <div style={qStyle}>4. Performance Categories</div>
              <div style={aStyle}>
                <b>Excellent (90–100 points):</b> High fitness level — retest in 12
                months.
                <br />
                <b>Satisfactory (75–89.9 points):</b> Meets standards — retest every 6
                months.
                <br />
                <b>Unsatisfactory (&lt;75 points):</b> Below standards — retest within
                90 days; possible administrative actions.
              </div>
            </div>
            <div style={sectionStyle}>
              <div style={qStyle}>5. Health-Risk Categories</div>
              <div style={aStyle}>
                Based on run time:
                <br />
                <b>Low Risk:</b> Strong cardiovascular fitness.
                <br />
                <b>Moderate Risk:</b> Room for improvement.
                <br />
                <b>High Risk:</b> Potential cardiovascular concerns; may require
                medical follow-up.
              </div>
            </div>
            <div style={sectionStyle}>
              <div style={qStyle}>6. Can I Take a Diagnostic (Practice) PT Test Early?</div>
              <div style={aStyle}>
                Yes, within 15 days before your official test (if current and not
                medically exempt).
                <br />
                Diagnostic tests don’t count officially but help assess readiness.
              </div>
            </div>
            <div style={sectionStyle}>
              <div style={qStyle}>7. PT Test Frequency</div>
              <div style={aStyle}>
                Based on your last official score:
                <br />
                <b>Excellent:</b> Once per year.
                <br />
                <b>Satisfactory:</b> Every 6 months.
                <br />
                <b>Unsatisfactory:</b> Within 90 days (guidance from leadership may
                apply).
              </div>
            </div>
            <div style={sectionStyle}>
              <div style={qStyle}>8. Impact of Medical Exemptions</div>
              <div style={aStyle}>
                Documented via AF Form 469 (temporary or permanent).
                <br />
                Scores are recalculated proportionally based on completed components.
              </div>
            </div>
            <div style={sectionStyle}>
              <div style={qStyle}>9. Alternative Cardio Options</div>
              <div style={aStyle}>
                Available only with a medical waiver:
                <br />
                Walk Test (for specific medical conditions)
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
