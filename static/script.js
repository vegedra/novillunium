// Referências globais
const music = document.getElementById("bg_music");
const soundButton = document.getElementById("sound_button");
const cmdInput = document.getElementById("cmd_input");

let musicStarted = false;
let musicPaused = true;
let musicMuted = true;

// Alterna música (botão canto superior direito)
function toggleMusic() {
    if(musicPaused || musicMuted){
        music.play();
        musicPaused = false;
        musicMuted = false;
        soundButton.innerText = "🔊";
    } else {
        music.pause();
        musicPaused = true;
        soundButton.innerText = "🔇";
    }
}

// Inicia música no primeiro comando, só se não estiver mutada
function startMusic() {
    if(!musicStarted && !musicMuted){
        music.play();
        musicStarted = true;
        musicPaused = false;
        soundButton.innerText = "🔊";
    }
}

// Envia o comando digitado
function enviarComando() {
    startMusic(); // só inicia se não estiver mutada

    const cmd = cmdInput.value.trim();
    if(cmd === "") return;

    fetch("/comando", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({cmd: cmd})
    })
    .then(response => response.json())
    .then(data => {
        // Atualiza sala e descrição
        document.getElementById("room_name").innerText = data.room_name;
        document.getElementById("room_desc").innerText = data.room_desc;
        document.getElementById("message").innerText = data.message;

        // Atualiza inventário
        const inv = document.getElementById("inventory_list");
        inv.innerHTML = "";
        if(data.inventory.length === 0) {
            const li = document.createElement("li");
            li.innerText = "Vazio";
            inv.appendChild(li);
        } else {
            data.inventory.forEach(item => {
                const li = document.createElement("li");
                li.innerText = item;
                inv.appendChild(li);
            });
        }

        cmdInput.value = "";
        cmdInput.focus();
    });
}

// Adiciona listener para Enter
window.onload = function() {
    cmdInput.addEventListener("keyup", function(event) {
        if(event.key === "Enter") enviarComando();
    });
};
