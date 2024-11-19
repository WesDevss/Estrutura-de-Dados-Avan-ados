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
        
        // Função para exibir recomendações na tela
        function exibirRecomendacoes(recomendacoes) {
            const container = document.getElementById("recomendacoes-container");
            container.innerHTML = "<h2>Recomendações:</h2><ul>" +
            recomendacoes.map((rec) => `<li>${rec}</li>`).join("") +
            "</ul>";
        }
        