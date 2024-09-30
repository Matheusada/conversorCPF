document.getElementById('cpf-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const entrada = document.getElementById('entrada').value.replace(/\s+/g, ''); // Remove espaços extras
    const cpfsFormatados = formatarCpfs(entrada);

    document.getElementById('cpfs-formatados').textContent = cpfsFormatados.join('\n');
});

// Função para formatar os CPFs
function formatarCpfs(entrada) {
    const cpfs = [];
    
    for (let i = 0; i < entrada.length; i += 11) {
        const numero = entrada.substring(i, i + 11);
        
        if (numero.length === 11) {
            const cpfFormatado = `${numero.slice(0, 3)}.${numero.slice(3, 6)}.${numero.slice(6, 9)}-${numero.slice(9)}`;
            cpfs.push(cpfFormatado);
        }
    }
    
    return cpfs;
}
