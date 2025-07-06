import React, { useState, useEffect } from "react";

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

const styles = {
  container: {
    maxWidth: 480,
    margin: "2rem auto",
    padding: 24,
    borderRadius: 16,
    background: "#f8fafc",
    boxShadow: "0 2px 16px 0 rgba(0,0,0,0.08)",
    fontFamily: "system-ui, sans-serif",
  },
  heading: {
    color: "#003366",
    textAlign: "center",
    marginBottom: 24,
    fontWeight: 700,
    fontSize: 28,
    letterSpacing: 1,
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: 16,
  },
  label: {
    fontWeight: 500,
    marginBottom: 4,
    color: "#222",
  },
  input: {
    padding: 10,
    borderRadius: 8,
    border: "1px solid #b0b8c1",
    fontSize: 16,
    marginBottom: 8,
    width: "100%",
    boxSizing: "border-box",
  },
  button: {
    background: "#003366",
    color: "#fff",
    border: "none",
    borderRadius: 8,
    padding: "12px 0",
    fontWeight: 600,
    fontSize: 18,
    marginTop: 8,
    cursor: "pointer",
    transition: "background 0.2s",
  },
  card: {
    background: "#fff",
    borderRadius: 12,
    boxShadow: "0 1px 6px 0 rgba(0,0,0,0.06)",
    padding: 16,
    marginTop: 20,
  },
  resultLabel: {
    fontWeight: 600,
    color: "#003366",
    marginRight: 8,
  },
  error: {
    color: "#b00020",
    marginTop: 16,
    textAlign: "center",
  },
  '@media (maxWidth: 600px)': {
    container: { padding: 8, maxWidth: '98vw' },
    heading: { fontSize: 22 },
    button: { fontSize: 16 },
  },
};

function App() {
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

  // Use conditional styles for mobile
  const mobileStyles = isMobile ? {
    container: { ...styles.container, padding: 8, maxWidth: '100vw' },
    heading: { ...styles.heading, fontSize: 22 },
    input: { ...styles.input, fontSize: 20, padding: 16, minHeight: 48 },
    button: { ...styles.button, fontSize: 20, padding: '18px 0', minHeight: 56, touchAction: 'manipulation' },
    label: { ...styles.label, fontSize: 18 },
    form: { ...styles.form, gap: 24 },
    card: { ...styles.card, fontSize: 18 },
    resultLabel: { ...styles.resultLabel, fontSize: 18 },
    error: { ...styles.error, fontSize: 16 },
  } : styles;

  return (
    <div style={mobileStyles.container}>
      <div style={mobileStyles.heading}>USAF PT Test Calculator</div>
      <form style={mobileStyles.form} onSubmit={handleSubmit} autoComplete="off">
        <label style={mobileStyles.label}>
          Gender
          <select
            style={mobileStyles.input}
            value={gender}
            onChange={e => setGender(e.target.value)}
          >
            <option value="male">Male</option>
            <option value="female">Female</option>
          </select>
        </label>
        <label style={mobileStyles.label}>
          Age
          <input
            style={mobileStyles.input}
            type="number"
            value={age}
            min={17}
            max={100}
            onChange={e => setAge(e.target.value)}
            required
            inputMode="numeric"
          />
        </label>
        {/* Cardio selection */}
        <label style={mobileStyles.label}>
          Cardio Component
          <select style={mobileStyles.input} value={cardioComp} onChange={e => setCardioComp(e.target.value)}>
            {CARDIO_OPTIONS.map(opt => <option key={opt.key} value={opt.key}>{opt.label}</option>)}
          </select>
        </label>
        <label style={mobileStyles.label}>
          {getOption("cardio", cardioComp).label}
          <input
            style={{...mobileStyles.input, borderColor: fieldErrors.cardio ? '#b00020' : mobileStyles.input.borderColor}}
            type={getOption("cardio", cardioComp).type === "time" ? "text" : getOption("cardio", cardioComp).type}
            name={cardioComp}
            value={values[cardioComp]}
            onChange={handleChange}
            placeholder={getOption("cardio", cardioComp).type === "time" ? "mm:ss" : undefined}
            required
            inputMode={getOption("cardio", cardioComp).type === "number" ? "numeric" : undefined}
          />
          {fieldErrors.cardio && <div style={{color:'#b00020', fontSize:13}}>{fieldErrors.cardio}</div>}
          {fieldWarnings.cardio && <div style={{color:'#b08000', fontSize:13}}>{fieldWarnings.cardio}</div>}
          <span style={{ fontSize: 13, color: '#555', marginLeft: 6 }}>
            {cardioComp === "run" && minMax.cardio?.max !== undefined && (
              `Max: ${formatMMSS(minMax.cardio.max)}`
            )}
            {cardioComp !== "run" && minMax.cardio?.min !== undefined && minMax.cardio?.max !== undefined && (
              `Min: ${minMax.cardio.min}, Max: ${minMax.cardio.max}`
            )}
          </span>
        </label>
        {/* Upper selection */}
        <label style={mobileStyles.label}>
          Upper Body Component
          <select style={mobileStyles.input} value={upperComp} onChange={e => setUpperComp(e.target.value)}>
            {UPPER_OPTIONS.map(opt => <option key={opt.key} value={opt.key}>{opt.label}</option>)}
          </select>
        </label>
        <label style={mobileStyles.label}>
          {getOption("upper", upperComp).label}
          <input
            style={{...mobileStyles.input, borderColor: fieldErrors.upper ? '#b00020' : mobileStyles.input.borderColor}}
            type={getOption("upper", upperComp).type}
            name={upperComp}
            value={values[upperComp]}
            onChange={handleChange}
            required
            inputMode={getOption("upper", upperComp).type === "number" ? "numeric" : undefined}
          />
          {fieldErrors.upper && <div style={{color:'#b00020', fontSize:13}}>{fieldErrors.upper}</div>}
          {fieldWarnings.upper && <div style={{color:'#b08000', fontSize:13}}>{fieldWarnings.upper}</div>}
          <span style={{ fontSize: 13, color: '#555', marginLeft: 6 }}>
            {minMax.upper?.min !== undefined && minMax.upper?.max !== undefined && (
              `Min: ${minMax.upper.min}, Max: ${minMax.upper.max}`
            )}
          </span>
        </label>
        {/* Core selection */}
        <label style={mobileStyles.label}>
          Core Component
          <select style={mobileStyles.input} value={coreComp} onChange={e => setCoreComp(e.target.value)}>
            {CORE_OPTIONS.map(opt => <option key={opt.key} value={opt.key}>{opt.label}</option>)}
          </select>
        </label>
        <label style={mobileStyles.label}>
          {getOption("core", coreComp).label}
          <input
            style={{...mobileStyles.input, borderColor: fieldErrors.core ? '#b00020' : mobileStyles.input.borderColor}}
            type={getOption("core", coreComp).type === "time" ? "text" : getOption("core", coreComp).type}
            name={coreComp}
            value={values[coreComp]}
            onChange={handleChange}
            placeholder={getOption("core", coreComp).type === "time" ? "mm:ss" : undefined}
            required
            inputMode={getOption("core", coreComp).type === "number" ? "numeric" : undefined}
          />
          {fieldErrors.core && <div style={{color:'#b00020', fontSize:13}}>{fieldErrors.core}</div>}
          {fieldWarnings.core && <div style={{color:'#b08000', fontSize:13}}>{fieldWarnings.core}</div>}
          <span style={{ fontSize: 13, color: '#555', marginLeft: 6 }}>
            {coreComp !== "plank" && minMax.core?.min !== undefined && minMax.core?.max !== undefined && (
              `Min: ${minMax.core.min}, Max: ${minMax.core.max}`
            )}
          </span>
        </label>
        <button style={mobileStyles.button} type="submit">
          Calculate
        </button>
        {error && <div style={mobileStyles.error}>{error}</div>}
      </form>
      {result && (
        <div style={mobileStyles.card}>
          <div style={{ fontWeight: 700, marginBottom: 12, fontSize: 18, color: '#003366' }}>
            Results
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <div style={mobileStyles.resultLabel}>Cardio:</div>
              <div style={{ fontWeight: 500, color: '#222' }}>
                {result.cardio.component === "run" ? formatMMSS(result.cardio.value) : result.cardio.value}
              </div>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <div style={mobileStyles.resultLabel}>Upper Body:</div>
              <div style={{ fontWeight: 500, color: '#222' }}>{result.upper.value}</div>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <div style={mobileStyles.resultLabel}>Core:</div>
              <div style={{ fontWeight: 500, color: '#222' }}>
                {result.core.component === "plank" ? formatMMSS(result.core.value) : result.core.value}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
