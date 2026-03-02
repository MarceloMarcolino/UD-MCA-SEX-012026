// Parte 2 – Objeto
// Crie um objeto com: nome, genero, preco, estoque

let filme = {
    nome: 'Interestelar',
    genero: 'Ficção Científica',
    preco: 39.90,
    estoque: 120
};

// =====================================================
// A. Como acessar o nome do objeto?
// =====================================================
console.log('=== Pergunta A ===');
console.log('Nome do objeto (notação de ponto):', filme.nome);

// =====================================================
// B. Como acessar o preço usando colchetes?
// =====================================================
console.log('\n=== Pergunta B ===');
console.log('Preço do objeto (notação de colchetes):', filme['preco']);

// =====================================================
// C. Atualize o estoque para 80.
// =====================================================
console.log('\n=== Pergunta C ===');
console.log('Estoque antes da atualização:', filme.estoque);
filme.estoque = 80;
console.log('Estoque após a atualização:', filme.estoque);

// =====================================================
// D. Imprima todas as propriedades no console.
// =====================================================
console.log('\n=== Pergunta D ===');
console.log('Todas as propriedades do objeto:');
for (let propriedade in filme) {
    console.log(propriedade + ': ' + filme[propriedade]);
}