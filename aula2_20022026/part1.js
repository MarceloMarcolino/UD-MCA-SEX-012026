// Parte 1 – Array Simples
// Array com pelo menos 20 elementos diferentes (nomes de jogos)

let jogos = [
    'Minecraft',           // 0
    'GTA V',               // 1
    'Tetris',              // 2
    'The Witcher 3',       // 3
    'Red Dead Redemption 2', // 4
    'God of War',          // 5
    'Elden Ring',          // 6
    'Fortnite',            // 7
    'Zelda: Breath of the Wild', // 8
    'Super Mario Odyssey', // 9
    'Resident Evil 4',     // 10
    'Counter-Strike 2',    // 11
    'League of Legends',   // 12
    'Valorant',            // 13
    'Overwatch 2',         // 14
    'FIFA 24',             // 15
    'Halo Infinite',       // 16
    'Cyberpunk 2077',      // 17
    'Dark Souls 3',        // 18
    'Bloodborne',          // 19
    'Sekiro',              // 20
];

// =====================================================
// A. Qual elemento está na posição 0, 7, 11, 15, 18 e 20?
// =====================================================
console.log('=== Pergunta A ===');
console.log('Posição 0:', jogos[0]);   // Minecraft
console.log('Posição 7:', jogos[7]);   // Fortnite
console.log('Posição 11:', jogos[11]); // Counter-Strike 2
console.log('Posição 15:', jogos[15]); // FIFA 24
console.log('Posição 18:', jogos[18]); // Dark Souls 3
console.log('Posição 20:', jogos[20]); // Sekiro

// =====================================================
// B. Qual elemento está na penúltima e última posição?
// =====================================================
console.log('\n=== Pergunta B ===');
console.log('Penúltima posição (' + (jogos.length - 2) + '):', jogos[jogos.length - 2]); // Bloodborne
console.log('Última posição (' + (jogos.length - 1) + '):', jogos[jogos.length - 1]);     // Sekiro

// =====================================================
// C. Quantos elementos existem no array?
// =====================================================
console.log('\n=== Pergunta C ===');
console.log('Quantidade de elementos:', jogos.length); // 21

// =====================================================
// D. Adicione um novo elemento ao final do array.
// =====================================================
console.log('\n=== Pergunta D ===');
jogos.push('Horizon Forbidden West');
console.log('Novo elemento adicionado: Horizon Forbidden West');
console.log('Nova quantidade de elementos:', jogos.length); // 22

// =====================================================
// E. Imprima todos os elementos usando um for.
// =====================================================
console.log('\n=== Pergunta E ===');
console.log('Todos os elementos do array:');
for (let i = 0; i < jogos.length; i++) {
    console.log('Posição ' + i + ': ' + jogos[i]);
}