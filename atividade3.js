// Parte 3 – Array de Objetos
// Array com pelo menos 10 objetos contendo: nome, preco, estoque (aluguel/venda)

let filmes = [
    { nome: 'Vingadores: Ultimato',     preco: 29.90,  estoque: 50 },
    { nome: 'Titanic',                  preco: 19.90,  estoque: 30 },
    { nome: 'Avatar: O Caminho da Água', preco: 34.90,  estoque: 40 },
    { nome: 'O Poderoso Chefão',        preco: 24.90,  estoque: 25 },
    { nome: 'Batman: O Cavaleiro das Trevas', preco: 22.90, estoque: 60 },
    { nome: 'Interestelar',             preco: 27.90,  estoque: 45 },
    { nome: 'Matrix',                   preco: 15.90,  estoque: 35 },
    { nome: 'Jurassic Park',            preco: 18.90,  estoque: 20 },
    { nome: 'O Senhor dos Anéis',       preco: 32.90,  estoque: 55 },
    { nome: 'Harry Potter e a Pedra Filosofal', preco: 21.90, estoque: 70 },
    { nome: 'Star Wars: O Império Contra-Ataca', preco: 26.90, estoque: 42 },
    { nome: 'Pulp Fiction',             preco: 23.90,  estoque: 15 }
];

// =====================================================
// A. Qual é o preço do segundo filme?
// =====================================================
console.log('=== Pergunta A ===');
console.log('Preço do segundo filme (' + filmes[1].nome + '):', 'R$ ' + filmes[1].preco.toFixed(2));

// =====================================================
// B. Qual é o nome do terceiro filme?
// =====================================================
console.log('\n=== Pergunta B ===');
console.log('Nome do terceiro filme:', filmes[2].nome);

// =====================================================
// C. Quantos filmes existem no array?
// =====================================================
console.log('\n=== Pergunta C ===');
console.log('Quantidade de filmes no array:', filmes.length);

// =====================================================
// D. Imprima o nome de todos os filmes.
// =====================================================
console.log('\n=== Pergunta D ===');
console.log('Nome de todos os filmes:');
for (let i = 0; i < filmes.length; i++) {
    console.log((i + 1) + '. ' + filmes[i].nome);
}

// =====================================================
// E. Some o total de cópias em estoque de todos os filmes.
// =====================================================
console.log('\n=== Pergunta E ===');
let totalEstoque = 0;
for (let i = 0; i < filmes.length; i++) {
    totalEstoque += filmes[i].estoque;
}
console.log('Total de cópias em estoque:', totalEstoque);

// =====================================================
// F. Qual filme possui maior estoque?
// =====================================================
console.log('\n=== Pergunta F ===');
let maiorEstoque = filmes[0];
for (let i = 1; i < filmes.length; i++) {
    if (filmes[i].estoque > maiorEstoque.estoque) {
        maiorEstoque = filmes[i];
    }
}
console.log('Filme com maior estoque:');
console.log('  Nome:', maiorEstoque.nome);
console.log('  Preço: R$', maiorEstoque.preco.toFixed(2));
console.log('  Estoque:', maiorEstoque.estoque);