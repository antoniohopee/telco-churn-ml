const TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
  "accent": "#6941C6",
  "ink": "#101828",
  "soft": "#F9FAFB",
  "fontFamily": "Inter",
  "headingScale": 100
}/*EDITMODE-END*/;

const FONT_OPTIONS = ["Inter", "IBM Plex Sans", "Geist", "Manrope", "DM Sans"];

function ensureFont(family) {
  const id = "tw-font-" + family.replace(/\s+/g, "-");
  if (document.getElementById(id)) return;
  const link = document.createElement("link");
  link.id = id;
  link.rel = "stylesheet";
  link.href = "https://fonts.googleapis.com/css2?family=" + family.replace(/\s+/g, "+") + ":wght@400;500;600;700;800&display=swap";
  document.head.appendChild(link);
}

function hexToRgb(hex) {
  const m = hex.replace("#", "");
  return [
    parseInt(m.substring(0, 2), 16),
    parseInt(m.substring(2, 4), 16),
    parseInt(m.substring(4, 6), 16)
  ];
}
function mix(hex, white = 0.88) {
  const [r, g, b] = hexToRgb(hex);
  return `rgb(${Math.round(r + (255 - r) * white)}, ${Math.round(g + (255 - g) * white)}, ${Math.round(b + (255 - b) * white)})`;
}
function darker(hex, amount = 0.25) {
  const [r, g, b] = hexToRgb(hex);
  return `rgb(${Math.round(r * (1 - amount))}, ${Math.round(g * (1 - amount))}, ${Math.round(b * (1 - amount))})`;
}

function App() {
  const [t, setTweak] = window.useTweaks(TWEAK_DEFAULTS);

  React.useEffect(() => {
    ensureFont(t.fontFamily);
    const root = document.documentElement;
    root.style.setProperty("--accent", t.accent);
    root.style.setProperty("--accent-soft", mix(t.accent, 0.88));
    root.style.setProperty("--accent-ink", darker(t.accent, 0.25));
    root.style.setProperty("--ink", t.ink);
    root.style.setProperty("--bg-soft", t.soft);
    root.style.setProperty("--font-sans", `"${t.fontFamily}", -apple-system, system-ui, sans-serif`);

    const scale = t.headingScale / 100;
    document.querySelectorAll("h1.title").forEach(el => { el.style.fontSize = (56 * scale) + "px"; });
    document.querySelectorAll(".cover .hero-title").forEach(el => { el.style.fontSize = (96 * scale) + "px"; });
    document.querySelectorAll(".divider .big").forEach(el => { el.style.fontSize = (120 * scale) + "px"; });
    document.querySelectorAll(".closing h1").forEach(el => { el.style.fontSize = (110 * scale) + "px"; });
  }, [t]);

  const { TweaksPanel, TweakSection, TweakColor, TweakSelect, TweakSlider } = window;

  return (
    <TweaksPanel title="Tweaks">
      <TweakSection label="Colori">
        <TweakColor label="Accent" value={t.accent}
          onChange={v => setTweak("accent", v)}
          options={["#6941C6", "#175CD3", "#101828", "#067647", "#B54708"]} />
        <TweakColor label="Inchiostro" value={t.ink}
          onChange={v => setTweak("ink", v)}
          options={["#101828", "#1D2939", "#000000", "#1A1A2E"]} />
        <TweakColor label="Sfondo morbido" value={t.soft}
          onChange={v => setTweak("soft", v)}
          options={["#F9FAFB", "#F4F4F5", "#FAFAF9", "#F8F5F0"]} />
      </TweakSection>

      <TweakSection label="Tipografia">
        <TweakSelect label="Font" value={t.fontFamily} options={FONT_OPTIONS}
          onChange={v => setTweak("fontFamily", v)} />
        <TweakSlider label="Scala titoli" value={t.headingScale}
          min={80} max={120} step={2} unit="%"
          onChange={v => setTweak("headingScale", v)} />
      </TweakSection>
    </TweaksPanel>
  );
}

const mountEl = document.createElement("div");
document.body.appendChild(mountEl);
ReactDOM.createRoot(mountEl).render(<App />);
