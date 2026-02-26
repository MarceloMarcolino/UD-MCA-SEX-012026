// Parte 2 – Objeto
// Crie um objeto com: nome, cor, preco, estoque

let jogo = {
    nome: 'The Witcher 3: Wild Hunt',
    cor: 'Preto',
    preco: 79.90,
    estoque: 150
};

// =====================================================
// A. Como acessar o nome do objeto?
// =====================================================
console.log('=== Pergunta A ===');
console.log('Nome do objeto (notação de ponto):', jogo.nome);

// =====================================================
// B. Como acessar o preço usando colchetes?
// =====================================================
console.log('\n=== Pergunta B ===');
console.log('Preço do objeto (notação de colchetes):', jogo['preco']);

// =====================================================
// C. Atualize o estoque para 80.
// =====================================================
console.log('\n=== Pergunta C ===');
console.log('Estoque antes da atualização:', jogo.estoque);
jogo.estoque = 80;
console.log('Estoque após a atualização:', jogo.estoque);

// =====================================================
// D. Imprima todas as propriedades no console.
// =====================================================
console.log('\n=== Pergunta D ===');
console.log('Todas as propriedades do objeto:');
for (let propriedade in jogo) {
    console.log(propriedade + ': ' + jogo[propriedade]);
}