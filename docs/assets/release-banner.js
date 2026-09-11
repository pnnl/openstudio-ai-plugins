window.OPENSTUDIO_AI_LATEST_RELEASE = {
  version: "0.3.0",
  url: "https://github.com/pnnl/openstudio-ai-plugins/releases/tag/v0.3.0",
  summary: "MCP contract 4: refresh or reinstall the plugin and reconnect the MCP server."
};

document.addEventListener("DOMContentLoaded", () => {
  const release = window.OPENSTUDIO_AI_LATEST_RELEASE;
  if (!release || !release.version || !release.url) return;

  document.querySelectorAll("[data-release-banner]").forEach((banner) => {
    const wrap = document.createElement("div");
    wrap.className = "wrap release-banner-content";

    const label = document.createElement("span");
    label.className = "release-label";
    label.textContent = "Latest release";

    const version = document.createElement("strong");
    version.textContent = `OpenStudio AI ${release.version}`;

    const summary = document.createElement("span");
    summary.className = "release-summary";
    summary.textContent = release.summary || "See the release notes for changes and upgrade guidance.";

    const link = document.createElement("a");
    link.href = release.url;
    link.textContent = "Read release notes ↗";

    wrap.append(label, version, summary, link);
    banner.append(wrap);
    banner.hidden = false;
  });
});
