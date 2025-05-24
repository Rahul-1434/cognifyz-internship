function updateSubtypes() {
    const chart = document.getElementById("chart").value;
    const subtypeSelect = document.getElementById("subtype");

    const subtypes = {
        matplotlib: ["hist", "scatter", "line"],
        seaborn: ["box", "violin", "heatmap"],
        plotly: ["scatter", "line", "box"]
    };

    subtypeSelect.innerHTML = "";

    if (chart && subtypes[chart]) {
        subtypes[chart].forEach(sub => {
            const opt = document.createElement("option");
            opt.value = sub;
            opt.textContent = sub.charAt(0).toUpperCase() + sub.slice(1);
            subtypeSelect.appendChild(opt);
        });
    }
}
