document$.subscribe(() => {
  initComputeEndurance();
  initComputeMigrants();
});

function initComputeEndurance() {
 const btn = document.getElementById("war-tables-compute-endurance-btn");
  const output = document.getElementById("war-tables-compute-endurance-result");
  const input = document.getElementById("war-tables-compute-endurance-input");
  if (!btn || !output || !input) {
    console.log("Endurance elements not found on this page");
    return;
  }
  btn.addEventListener("click", () => {
    const entry = Number.parseInt(input.value) || 0;
    const result = Math.pow(entry / 2, 1.5) * 20;
    const formatted = `+ ${Math.round(result)} %`;
    output.textContent = formatted;
    output.style.color = "var(--md-accent-fg-color)";
    output.classList.remove("result-pop");
    // reset animation
    void output.offsetWidth;
    output.classList.add("result-pop");
  });
}

function initComputeMigrants() {
  const btn = document.getElementById("races-compute-migrants-btn");
  const output = document.getElementById("races-compute-migrants-result");
  const input = document.getElementById("races-compute-migrants-input");
  if (!btn || !output || !input) {
    console.log("migrants elements not found on this page");
    return;
  }
  btn.addEventListener("click", () => {
    const entry = Number.parseInt(input.value) || 0;
    if (entry <= 0) { output.textContent = "-"; return; }
    const result = 20 * Math.log10(entry / 50);
    const formatted = `${Math.round(result)}`;
    output.textContent = formatted;
    output.style.color = "var(--md-accent-fg-color)";
    output.classList.remove("result-pop");
    // reset animation
    void output.offsetWidth;
    output.classList.add("result-pop");
  });
}
