// Parte 3 – Array de Objetos
// Array com pelo menos 10 objetos contendo: nome, preco, estoque

let produtos = [
    { nome: 'Minecraft',                preco: 119.90,  estoque: 200 },
    { nome: 'GTA V',                    preco: 89.90,   estoque: 150 },
    { nome: 'The Witcher 3',            preco: 79.90,   estoque: 120 },
    { nome: 'Red Dead Redemption 2',    preco: 149.90,  estoque: 90  },
    { nome: 'God of War',               preco: 199.90,  estoque: 75  },
    { nome: 'Elden Ring',               preco: 249.90,  estoque: 300 },
    { nome: 'Fortnite',                 preco: 0.00,    estoque: 999 },
    { nome: 'Counter-Strike 2',         preco: 0.00,    estoque: 500 },
    { nome: 'FIFA 24',                  preco: 299.90,  estoque: 60  },
    { nome: 'Cyberpunk 2077',           preco: 199.90,  estoque: 110 },
    { nome: 'Dark Souls 3',             preco: 99.90,   estoque: 85  },
    { nome: 'Zelda: Breath of the Wild', preco: 299.90, estoque: 45  }
];

// =====================================================
// A. Qual é o preço do segundo objeto?
// =====================================================
console.log('=== Pergunta A ===');
console.log('Preço do segundo objeto (' + produtos[1].nome + '):', 'R$ ' + produtos[1].preco.toFixed(2));

// =====================================================
// B. Qual é o nome do terceiro objeto?
// =====================================================
console.log('\n=== Pergunta B ===');
console.log('Nome do terceiro objeto:', produtos[2].nome);

// =====================================================
// C. Quantos itens existem no array?
// =====================================================
console.log('\n=== Pergunta C ===');
console.log('Quantidade de itens no array:', produtos.length);

// =====================================================
// D. Imprima o nome de todos os objetos.
// =====================================================
console.log('\n=== Pergunta D ===');
console.log('Nome de todos os objetos:');
for (let i = 0; i < produtos.length; i++) {
    console.log((i + 1) + '. ' + produtos[i].nome);
}

// =====================================================
// E. Some o total de estoque de todos os objetos.
// =====================================================
console.log('\n=== Pergunta E ===');
let totalEstoque = 0;
for (let i = 0; i < produtos.length; i++) {
    totalEstoque += produtos[i].estoque;
}
console.log('Total de estoque de todos os objetos:', totalEstoque);

// =====================================================
// F. Qual objeto possui maior estoque?
// =====================================================
console.log('\n=== Pergunta F ===');
let maiorEstoque = produtos[0];
for (let i = 1; i < produtos.length; i++) {
    if (produtos[i].estoque > maiorEstoque.estoque) {
        maiorEstoque = produtos[i];
    }
}
console.log('Objeto com maior estoque:');
console.log('  Nome:', maiorEstoque.nome);
console.log('  Preço: R$', maiorEstoque.preco.toFixed(2));
console.log('  Estoque:', maiorEstoque.estoque);