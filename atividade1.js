let filmes = [
    'Vingadores: Ultimato',          // 0
    'Titanic',                       // 1
    'Avatar',                        // 2
    'O Poderoso Chefão',             // 3
    'Batman: O Cavaleiro das Trevas',// 4
    'Interestelar',                  // 5
    'Matrix',                        // 6
    'Gladiador',                     // 7
    'Jurassic Park',                 // 8
    'O Senhor dos Anéis',            // 9
    'Homem-Aranha',                  // 10
    'Pantera Negra',                 // 11
    'Toy Story',                     // 12
    'Shrek',                         // 13
    'Harry Potter',                  // 14
    'Star Wars',                     // 15
    'A Origem',                      // 16
    'Coringa',                       // 17
    'Frozen',                        // 18
    'Velozes e Furiosos',            // 19
    'Deadpool',                      // 20
];

// =====================================================
// A. Qual elemento está na posição 0, 7, 11, 15, 18 e 20?
// =====================================================
console.log('=== Pergunta A ===');
console.log('Posição 0:', filmes[0]);
console.log('Posição 7:', filmes[7]);
console.log('Posição 11:', filmes[11]);
console.log('Posição 15:', filmes[15]);
console.log('Posição 18:', filmes[18]);
console.log('Posição 20:', filmes[20]);

// =====================================================
// B. Qual elemento está na penúltima e última posição?
// =====================================================
console.log('\n=== Pergunta B ===');
console.log('Penúltima posição (' + (filmes.length - 2) + '):', filmes[filmes.length - 2]);
console.log('Última posição (' + (filmes.length - 1) + '):', filmes[filmes.length - 1]);

// =====================================================
// C. Quantos elementos existem no array?
// =====================================================
console.log('\n=== Pergunta C ===');
console.log('Quantidade de elementos:', filmes.length);

// =====================================================
// D. Adicione um novo elemento ao final do array.
// =====================================================
console.log('\n=== Pergunta D ===');
filmes.push('Homem de Ferro');
console.log('Novo elemento adicionado: Homem de Ferro');
console.log('Nova quantidade de elementos:', filmes.length);

// =====================================================
// E. Imprima todos os elementos usando um for.
// =====================================================
console.log('\n=== Pergunta E ===');
console.log('Todos os elementos do array:');
for (let i = 0; i < filmes.length; i++) {
    console.log('Posição ' + i + ': ' + filmes[i]);
}