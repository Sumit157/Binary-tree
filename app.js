const timeline = [
  { title: "Before election announcement", detail: "Check your name in the electoral roll and confirm details." },
  { title: "Registration/revision window", detail: "Apply for new registration or corrections through official channels." },
  { title: "Campaign period", detail: "Review candidate details, constituency info, and official notices." },
  { title: "Polling week", detail: "Verify booth location, polling time, and accepted identity documents." },
  { title: "Polling day", detail: "Vote using EVM/VVPAT at your assigned polling station." },
  { title: "After polling", detail: "Follow official counting and result announcements." }
];

const steps = [
  ["Check eligibility", "Ensure you are 18+ and eligible as per Indian election rules."],
  ["Register to vote", "If needed, apply as a new voter via official election services."],
  ["Correct details", "Request corrections if your name, address, or details are incorrect."],
  ["Verify electoral roll", "Confirm your name appears in the final electoral roll before polling."],
  ["Locate polling booth", "Check your assigned polling station and reporting time."],
  ["Carry accepted ID", "Bring EPIC or other accepted identification as officially notified."],
  ["Cast your vote", "Follow polling staff instructions and use EVM/VVPAT."],
  ["Track updates", "Use official channels for result and post-poll updates."]
];

const faqs = [
  { q: "How do I register to vote in India?", a: "Use official election registration services and submit the required details/documents before the deadline." },
  { q: "What is EPIC?", a: "EPIC is the Electors Photo Identity Card, commonly called voter ID." },
  { q: "Can I vote without voter ID card?", a: "In many cases alternate accepted ID documents are allowed, based on official poll notifications." },
  { q: "What are EVM and VVPAT?", a: "EVM is the Electronic Voting Machine and VVPAT provides a voter-verifiable paper audit trail." },
  { q: "How do I find my polling booth?", a: "Check official voter services using your elector details or constituency info." }
];

function renderTimeline() {
  const container = document.getElementById("timeline-cards");
  container.innerHTML = "";
  timeline.forEach((item, i) => {
    const card = document.createElement("article");
    card.className = "card";
    card.innerHTML = `<h4>${i + 1}. ${item.title}</h4><small>${item.detail}</small>`;
    container.appendChild(card);
  });
}

function renderSteps() {
  const container = document.getElementById("steps-list");
  steps.forEach(([title, detail], i) => {
    const div = document.createElement("div");
    div.className = "step";
    div.innerHTML = `<strong>${i + 1}) ${title}</strong><p>${detail}</p>`;
    container.appendChild(div);
  });
}

function buildPlan(state, status, language) {
  const checklist = [
    `Confirm electoral roll status for ${state}.`,
    "Check your polling booth location and polling schedule.",
    "Review accepted ID documents from official poll notice.",
    "Keep election day essentials ready one day before voting."
  ];

  if (status === "not_registered") {
    checklist.unshift("Apply for new voter registration using official election services.");
  } else if (status === "not_sure") {
    checklist.unshift("First verify whether your name exists in the electoral roll.");
  }

  if (language === "hindi") {
    checklist.push("Use Hindi election guides/resources wherever available.");
  } else if (language === "regional") {
    checklist.push("Use state/regional language voter resources for clarity.");
  }

  return checklist;
}

function bindPlanner() {
  const form = document.getElementById("planner-form");
  const output = document.getElementById("plan-output");

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const state = document.getElementById("state").value.trim();
    const status = document.getElementById("status").value;
    const language = document.getElementById("language").value;

    const checklist = buildPlan(state, status, language);
    output.classList.remove("hidden");
    output.innerHTML = `<h4>Your Personalized Voting Checklist</h4><ul>${checklist
      .map((item) => `<li>${item}</li>`)
      .join("")}</ul>`;
  });
}

function renderFaq(list = faqs) {
  const container = document.getElementById("faq-list");
  container.innerHTML = "";

  if (!list.length) {
    container.innerHTML = `<div class="faq-item"><strong>No direct match found.</strong><p>Please verify this on official ECI/state election resources.</p></div>`;
    return;
  }

  list.forEach((item) => {
    const div = document.createElement("div");
    div.className = "faq-item";
    div.innerHTML = `<strong>${item.q}</strong><p>${item.a}</p>`;
    container.appendChild(div);
  });
}

function bindFaqSearch() {
  const search = document.getElementById("faq-search");
  search.addEventListener("input", (e) => {
    const q = e.target.value.toLowerCase().trim();
    if (!q) {
      renderFaq();
      return;
    }
    const filtered = faqs.filter((item) => `${item.q} ${item.a}`.toLowerCase().includes(q));
    renderFaq(filtered);
  });
}

renderTimeline();
renderSteps();
bindPlanner();
renderFaq();
bindFaqSearch();
