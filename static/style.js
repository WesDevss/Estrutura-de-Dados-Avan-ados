// Função para fazer requisição ao backend
function recomendar(serie) {
    fetch("/recomendar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ serie: serie }),
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.recomendacoes) {
            exibirRecomendacoes(data.recomendacoes);
        } else {
            alert(data.erro || "Erro ao obter recomendações.");
        }
    })
    .catch((error) => {
        console.error("Erro:", error);
        alert("Erro ao se comunicar com o servidor.");
    });
}

// Função para exibir recomendações em cartões
function exibirRecomendacoes(recomendacoes) {
    const container = document.getElementById("recomendacoes-container");
    container.innerHTML = "<h2>Recomendações:</h2>";
    const cards = document.createElement("div");
    cards.className = "recommendations";

    recomendacoes.forEach((rec) => {
        const card = document.createElement("div");
        card.className = "card";

        // Adiciona conteúdo dinâmico no cartão
        card.innerHTML = `
            <img src="/static/images/${rec.toLowerCase().replace(/ /g, "-")}.jpg" alt="${rec}">
            <h3>${rec}</h3>
            <p>Descrição fictícia da série: "${rec}".</p>
        `;

        cards.appendChild(card);
    });

    container.appendChild(cards);
}
