import React, { useState, useEffect } from "react";
import FAQ from "./FAQ";
import Contact from "./Contact";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

const CARDIO_OPTIONS = [
  { key: "run", label: "1.5 Mile Run (mm:ss)", type: "time" },
  { key: "hamr", label: "20m HAMR (shuttles)", type: "number" },
];
const UPPER_OPTIONS = [
  { key: "pushups", label: "1 min Push-ups (reps)", type: "number" },
  { key: "hr_pushups", label: "2 min Hand Release Push-ups (reps)", type: "number" },
];
const CORE_OPTIONS = [
  { key: "situps", label: "1 min Sit-ups (reps)", type: "number" },
  { key: "crunch", label: "2 min Cross Leg Reverse Crunch (reps)", type: "number" },
  { key: "plank", label: "Forearm Plank (mm:ss)", type: "time" },
];

function mmssToSeconds(mmss) {
  // Accepts 'mm:ss' or 'm:ss' or 'ss' or 'mss' or 'mmss' (auto-formats)
  if (!mmss) return 0;
  let clean = mmss.replace(/[^0-9]/g, "");
  if (clean.length <= 2) return parseInt(clean, 10) || 0;
  if (clean.length === 3) clean = '0' + clean; // e.g. 456 -> 0456
  let min = parseInt(clean.slice(0, -2), 10);
  let sec = parseInt(clean.slice(-2), 10);
  return min * 60 + sec;
}

function autoFormatMMSS(val) {
  // Auto-format to mm:ss as user types
  let clean = val.replace(/[^0-9]/g, "");
  if (clean.length === 0) return "";
  if (clean.length <= 2) return clean;
  if (clean.length === 3) return clean[0] + ":" + clean.slice(1); // e.g. 934 -> 9:34
  if (clean.length === 4) return clean.slice(0,2) + ":" + clean.slice(2); // e.g. 1024 -> 10:24
  // For longer input, just use last 4 digits
  if (clean.length > 4) return clean.slice(-4, -2) + ":" + clean.slice(-2);
  return clean;
}

function formatMMSS(seconds) {
  if (typeof seconds !== "number" || isNaN(seconds)) return "--:--";
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return `${m.toString().padStart(2, "0")}:${s.toString().padStart(2, "0")}`;
}

const palette = {
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

const styles = {
  container: {
    maxWidth: 480,
    margin: "2rem auto",
    padding: 24,
    borderRadius: 16,
    background: palette.bg,
    boxShadow: palette.cardShadow,
    fontFamily: "Inter, system-ui, Arial, sans-serif",
    color: palette.text,
    position: 'relative',
  },
  heading: {
    color: palette.text,
    textAlign: "center",
    marginBottom: 24,
    fontWeight: 700,
    fontSize: 28,
    letterSpacing: 1,
    fontFamily: "Inter, system-ui, Arial, sans-serif",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: 16,
  },
  label: {
    fontWeight: 500,
    marginBottom: 4,
    color: palette.label,
    fontFamily: "Inter, system-ui, Arial, sans-serif",
  },
  input: {
    padding: 10,
    borderRadius: 8,
    border: `1px solid ${palette.inputBorder}`,
    fontSize: 16,
    marginBottom: 8,
    width: "100%",
    boxSizing: "border-box",
    background: palette.inputBg,
    color: palette.inputText,
    fontFamily: "Inter, system-ui, Arial, sans-serif",
  },
  button: {
    background: palette.buttonBg,
    color: palette.buttonText,
    border: "none",
    borderRadius: 8,
    padding: "12px 0",
    fontWeight: 600,
    fontSize: 18,
    marginTop: 8,
    cursor: "pointer",
    transition: "background 0.2s",
    fontFamily: "Inter, system-ui, Arial, sans-serif",
  },
  card: {
    background: palette.card,
    borderRadius: 12,
    boxShadow: palette.cardShadow,
    padding: 16,
    marginTop: 20,
    fontFamily: "Inter, system-ui, Arial, sans-serif",
  },
  resultLabel: {
    fontWeight: 600,
    color: palette.resultLabel,
    marginRight: 8,
    fontFamily: "Inter, system-ui, Arial, sans-serif",
  },
  error: {
    color: palette.error,
    marginTop: 16,
    textAlign: "center",
    fontFamily: "Inter, system-ui, Arial, sans-serif",
  },
};

function AppContent() {
  const [gender, setGender] = useState("male");
  const [age, setAge] = useState(25);
  const [cardioComp, setCardioComp] = useState("run");
  const [upperComp, setUpperComp] = useState("pushups");
  const [coreComp, setCoreComp] = useState("situps");
  const [values, setValues] = useState({ run: "", hamr: "", pushups: "", hr_pushups: "", situps: "", crunch: "", plank: "" });
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [minMax, setMinMax] = useState({ cardio: {}, upper: {}, core: {} });
  const [fieldErrors, setFieldErrors] = useState({});
  const [fieldWarnings, setFieldWarnings] = useState({});
  const [isMobile, setIsMobile] = useState(false);
  const [showMenu, setShowMenu] = useState(false);

  useEffect(() => {
    // Mobile detection
    const checkMobile = () => {
      setIsMobile(window.innerWidth <= 600 || /Mobi|Android/i.test(navigator.userAgent));
    };
    checkMobile();
    window.addEventListener('resize', checkMobile);
    return () => window.removeEventListener('resize', checkMobile);
  }, []);

  // Fetch min/max when gender, age, or component selection changes
  useEffect(() => {
    async function fetchMinMax(cat, comp) {
      try {
        const res = await fetch(`/api/pt/minmax?gender=${gender}&age=${age}&component=${comp}`);
        const data = await res.json();
        setMinMax(prev => ({ ...prev, [cat]: data }));
      } catch {
        setMinMax(prev => ({ ...prev, [cat]: {} }));
      }
    }
    fetchMinMax("cardio", cardioComp);
    fetchMinMax("upper", upperComp);
    fetchMinMax("core", coreComp);
  }, [gender, age, cardioComp, upperComp, coreComp]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    if (name === "run" || name === "plank") {
      setValues({ ...values, [name]: autoFormatMMSS(value) });
    } else {
      setValues({ ...values, [name]: value });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setResult(null);
    setFieldErrors({});
    setFieldWarnings({});
    const newFieldErrors = {};
    const newFieldWarnings = {};
    // Cardio: allow out-of-range for both run and hamr, show warnings only
    const cardioVal = values[cardioComp];
    if (!cardioVal || (cardioComp === "run" && mmssToSeconds(cardioVal) <= 0) || (cardioComp !== "run" && Number(cardioVal) <= 0)) {
      newFieldErrors.cardio = "Enter a valid value";
    } else if (minMax.cardio?.min !== undefined && minMax.cardio?.max !== undefined) {
      const val = cardioComp === "run" ? mmssToSeconds(cardioVal) : Number(cardioVal);
      if (val < minMax.cardio.min) {
        newFieldWarnings.cardio = `Below minimum: will score max points.`;
      } else if (val > minMax.cardio.max) {
        newFieldWarnings.cardio = `Above maximum: will score 0 points.`;
      }
    }
    // Upper: allow out-of-range, show warning
    const upperVal = values[upperComp];
    if (!upperVal || Number(upperVal) <= 0) {
      newFieldErrors.upper = "Enter a valid value";
    } else if (minMax.upper?.min !== undefined && minMax.upper?.max !== undefined) {
      const val = Number(upperVal);
      if (val < minMax.upper.min) {
        newFieldWarnings.upper = `Below minimum: will score 0 points.`;
      } else if (val > minMax.upper.max) {
        newFieldWarnings.upper = `Above maximum: will score 20 points.`;
      }
    }
    // Core: allow out-of-range, show warning
    const coreVal = values[coreComp];
    if (!coreVal || (coreComp === "plank" && mmssToSeconds(coreVal) <= 0) || (coreComp !== "plank" && Number(coreVal) <= 0)) {
      newFieldErrors.core = "Enter a valid value";
    } else if (minMax.core?.min !== undefined && minMax.core?.max !== undefined) {
      const val = coreComp === "plank" ? mmssToSeconds(coreVal) : Number(coreVal);
      if (val < minMax.core.min) {
        newFieldWarnings.core = `Below minimum: will score 0 points.`;
      } else if (val > minMax.core.max) {
        newFieldWarnings.core = `Above maximum: will score 20 points.`;
      }
    }
    if (Object.keys(newFieldErrors).length > 0) {
      setFieldErrors(newFieldErrors);
      setFieldWarnings(newFieldWarnings);
      setError("Please correct the highlighted errors.");
      return;
    }
    setFieldWarnings(newFieldWarnings);
    const req = {
      gender,
      age: Number(age),
      cardio: { component: cardioComp, value: cardioComp === "run" ? mmssToSeconds(values[cardioComp]) : Number(values[cardioComp]) },
      upper: { component: upperComp, value: Number(values[upperComp]) },
      core: { component: coreComp, value: coreComp === "plank" ? mmssToSeconds(values[coreComp]) : Number(values[coreComp]) },
    };
    try {
      const res = await fetch("/api/pt/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(req),
      });
      const data = await res.json();
      console.log('API /api/pt/calculate response:', data); // DEBUG
      if (res.ok) setResult(data);
      else setError(data.message || "Error");
    } catch (err) {
      setError("Network error");
    }
  };

  const getOption = (cat, key) => {
    if (cat === "cardio") return CARDIO_OPTIONS.find(o => o.key === key);
    if (cat === "upper") return UPPER_OPTIONS.find(o => o.key === key);
    if (cat === "core") return CORE_OPTIONS.find(o => o.key === key);
    return null;
  };

  // Helper to get min/max for current selection, with mm:ss formatting for run/plank
  const getMinMax = (cat) => {
    const mm = minMax[cat] || {};
    if (cat === "cardio" && cardioComp === "run" && mm.max !== undefined) {
      // Only show max for run, in mm:ss
      return `Max: ${formatMMSS(mm.max)}`;
    }
    if (cat === "core" && coreComp === "plank" && mm.min !== undefined && mm.max !== undefined) {
      // Show min/max for plank, in mm:ss
      return `Min: ${formatMMSS(mm.min)}, Max: ${formatMMSS(mm.max)}`;
    }
    // All other cases: show min/max as numbers
    if (mm.min !== undefined && mm.max !== undefined) {
      return `Min: ${mm.min}, Max: ${mm.max}`;
    }
    if (mm.max !== undefined) {
      return `Max: ${mm.max}`;
    }
    return null;
  };

  // Helper to get overall rating
  const getOverallRating = (score) => {
    if (score === undefined || score === null) return "--";
    if (score < 75) return "Unsatisfactory";
    if (score < 90) return "Satisfactory";
    return "Excellent";
  };

  return (
    <div style={styles.container}>
      <div style={{ ...styles.heading, fontSize: 36, marginBottom: 32, letterSpacing: 0 }}>USAF PT Calc</div>
      <form onSubmit={handleSubmit} style={styles.form}>
        {/* Gender */}
        <div>
          <div style={styles.label}>Gender</div>
          <select
            name="gender"
            value={gender}
            onChange={e => setGender(e.target.value)}
            style={styles.input}
          >
            <option value="male">Male</option>
            <option value="female">Female</option>
          </select>
        </div>
        {/* Age */}
        <div>
          <div style={styles.label}>Age</div>
          <input
            type="number"
            name="age"
            value={age}
            onChange={e => setAge(e.target.value)}
            min={10}
            max={100}
            style={styles.input}
          />
        </div>
        {/* Cardio Component */}
        <div>
          <div style={styles.label}>Cardio Component</div>
          <select
            name="cardioComp"
            value={cardioComp}
            onChange={e => setCardioComp(e.target.value)}
            style={styles.input}
          >
            {CARDIO_OPTIONS.map(opt => (
              <option key={opt.key} value={opt.key}>
                {opt.label}
              </option>
            ))}
          </select>
        </div>
        {/* Cardio Value */}
        <div>
          <div style={styles.label}>{CARDIO_OPTIONS.find(opt => opt.key === cardioComp)?.label}</div>
          <input
            type={cardioComp === "run" ? "text" : "number"}
            name={cardioComp}
            value={values[cardioComp]}
            onChange={handleChange}
            style={styles.input}
            placeholder={cardioComp === "run" ? "mm:ss" : undefined}
          />
          <div style={{ fontSize: 15, color: palette.label, marginTop: 2 }}>{getMinMax("cardio")}</div>
          {fieldErrors.cardio && <div style={styles.error}>{fieldErrors.cardio}</div>}
          {fieldWarnings.cardio && <div style={{ ...styles.error, color: palette.warning }}>{fieldWarnings.cardio}</div>}
        </div>
        {/* Upper Component */}
        <div>
          <div style={styles.label}>Upper Body Component</div>
          <select
            name="upperComp"
            value={upperComp}
            onChange={e => setUpperComp(e.target.value)}
            style={styles.input}
          >
            {UPPER_OPTIONS.map(opt => (
              <option key={opt.key} value={opt.key}>
                {opt.label}
              </option>
            ))}
          </select>
        </div>
        {/* Upper Value */}
        <div>
          <div style={styles.label}>{UPPER_OPTIONS.find(opt => opt.key === upperComp)?.label}</div>
          <input
            type="number"
            name={upperComp}
            value={values[upperComp]}
            onChange={handleChange}
            style={styles.input}
          />
          <div style={{ fontSize: 15, color: palette.label, marginTop: 2 }}>{getMinMax("upper")}</div>
          {fieldErrors.upper && <div style={styles.error}>{fieldErrors.upper}</div>}
          {fieldWarnings.upper && <div style={{ ...styles.error, color: palette.warning }}>{fieldWarnings.upper}</div>}
        </div>
        {/* Core Component */}
        <div>
          <div style={styles.label}>Core Component</div>
          <select
            name="coreComp"
            value={coreComp}
            onChange={e => setCoreComp(e.target.value)}
            style={styles.input}
          >
            {CORE_OPTIONS.map(opt => (
              <option key={opt.key} value={opt.key}>
                {opt.label}
              </option>
            ))}
          </select>
        </div>
        {/* Core Value */}
        <div>
          <div style={styles.label}>{CORE_OPTIONS.find(opt => opt.key === coreComp)?.label}</div>
          <input
            type={coreComp === "plank" ? "text" : "number"}
            name={coreComp}
            value={values[coreComp]}
            onChange={handleChange}
            style={styles.input}
            placeholder={coreComp === "plank" ? "mm:ss" : undefined}
          />
          <div style={{ fontSize: 15, color: palette.label, marginTop: 2 }}>{getMinMax("core")}</div>
          {fieldErrors.core && <div style={styles.error}>{fieldErrors.core}</div>}
          {fieldWarnings.core && <div style={{ ...styles.error, color: palette.warning }}>{fieldWarnings.core}</div>}
        </div>
        <button type="submit" style={{ ...styles.button, fontSize: 28, marginTop: 24, borderRadius: 12, background: '#0a2d5c' }}>
          Calculate
        </button>
        {error && <div style={styles.error}>{error}</div>}
      </form>
      {/* Results Section */}
      {result && (
        <div style={styles.card}>
          <div style={styles.resultLabel}>Results</div>
          <div style={{ margin: "8px 0", color: palette.text }}>
            <div>Cardio Points: {result.cardio_points !== undefined ? result.cardio_points.toFixed(2) : "--"}</div>
            <div>Upper Points: {result.upper_points !== undefined ? result.upper_points.toFixed(2) : "--"}</div>
            <div>Core Points: {result.core_points !== undefined ? result.core_points.toFixed(2) : "--"}</div>
            <div>Total Score: {result.total_score !== undefined ? result.total_score.toFixed(2) : "--"}</div>
            <div>Overall Rating: {getOverallRating(result.total_score)}</div>
          </div>
        </div>
      )}
      {/* Footer */}
      <footer style={{ marginTop: 40, fontSize: 15, color: palette.text, textAlign: "center", opacity: 0.85 }}>
        <div>For bug reports, suggestions, and feedback, please feel free to email us at <a href="mailto:usafptcalc@protonmail.com" style={{ color: palette.accent, textDecoration: "underline" }}>usafptcalc@protonmail.com</a>.</div>
        <div>© 2025 USAF PT Calc. All rights reserved.</div>
        <div>This site is not endorsed by the U.S. Air Force.</div>
      </footer>
      {/* Menu Button */}
      <button
        onClick={() => setShowMenu(!showMenu)}
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
        aria-label="Open menu"
      >
        ☰
      </button>
      {/* Slide-out Menu */}
      {showMenu && (
        <div
          style={{
            position: "fixed",
            top: 0,
            right: 0,
            width: 260,
            height: "100vh",
            background: "#fff",
            boxShadow: "-2px 0 16px 0 rgba(0,0,0,0.12)",
            zIndex: 2000,
            padding: 24,
            display: "flex",
            flexDirection: "column",
            gap: 16,
          }}
        >
          <button
            onClick={() => setShowMenu(false)}
            style={{
              background: "none",
              border: "none",
              fontSize: 28,
              color: "#174ea6",
              alignSelf: "flex-end",
              cursor: "pointer",
            }}
            aria-label="Close menu"
          >
            ×
          </button>
          <Link to="/faq" style={{ color: "#174ea6", textDecoration: "none", fontWeight: 600 }}>FAQ</Link>
          <Link to="/contact" style={{ color: "#174ea6", textDecoration: "none", fontWeight: 600 }}>Contact</Link>
          <a href="https://www.afpc.af.mil/Portals/70/documents/FITNESS/dafman36-2905.pdf" target="_blank" rel="noopener noreferrer" style={{ color: "#174ea6", textDecoration: "none", fontWeight: 600 }}>DAFMAN 36-2905</a>
          <a href="https://www.afpc.af.mil/Portals/70/documents/FITNESS/5%20Year%20Chart%20Scoring%20Including%20Optional%20Component%20Standards%20-%2020211111%200219.pdf" target="_blank" rel="noopener noreferrer" style={{ color: "#174ea6", textDecoration: "none", fontWeight: 600 }}>Scoring Charts</a>
        </div>
      )}
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/faq" element={<FAQ />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="*" element={<AppContent />} />
      </Routes>
    </Router>
  );
}

export default App;
