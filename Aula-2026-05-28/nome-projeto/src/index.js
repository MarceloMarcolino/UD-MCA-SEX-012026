import React from 'react'; 
import { createRoot } from 'react-dom/client'; 
import App from './components/App'; 
//Importa o tema 
import 'primereact/resources/themes/bootstrap4-light-purple/theme.css';  
import 'primereact/resources/primereact.min.css';  // Estilo base do PrimeReact 
import 'primeicons/primeicons.css';               // Ícones 
import 'primeflex/primeflex.css';                // Utilitários CSS (layout/flex) 
 
const container = document.getElementById('root'); 
const root = createRoot(container); 
 
root.render(<App />); 