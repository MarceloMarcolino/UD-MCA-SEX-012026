import React from 'react'
import { createRoot } from 'react-dom/client'
import 'bootstrap/dist/css/bootstrap.min.css'
class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            latitude: null,
            longitude: null,
            estacao: null,
            data: null,
            icone: null,
            mensagemDeErro: null
        }
    }

    obterEstacao = (dataOriginal, latitude) => {
        const ano = dataOriginal.getFullYear();
        const diaAno = (data) =>
            new Date(data.getFullYear(), data.getMonth(), data.getDate());
        const data = diaAno(dataOriginal); // zera hora
        const dPrimavera = new Date(ano, 8, 23); // 23/09
        const dVerao = new Date(ano, 11, 21); // 21/12
        const dOutono = new Date(ano, 2, 20); // 20/03
        const dInverno = new Date(ano, 5, 21); // 21/06
        const hemisferioSul = latitude < 0;
        if (hemisferioSul) {
            if (data >= dOutono && data < dInverno) return "Outono";
            if (data >= dInverno && data < dPrimavera) return "Inverno";
            if (data >= dPrimavera && data < dVerao) return "Primavera";
            return "Verão";
        } else {
            if (data >= dOutono && data < dInverno) return "Primavera";
            if (data >= dInverno && data < dPrimavera) return "Verão";
            if (data >= dPrimavera && data < dVerao) return "Outono";
            return "Inverno";
        }
    };
    icones = {
        'Primavera': 'fa-seedling',
        'Verão': 'fa-umbrella-beach',
        'Outono': 'fa-tree',
        'Inverno': 'fa-snowman'
    }

    obterLocalizacao = () => {
        window.navigator.geolocation.getCurrentPosition(
            (posicao) => {
                let data = new Date()
                let estacao = this.obterEstacao(data, posicao.coords.latitude);
                let icone = this.icones[estacao]
                console.log(icone)
                this.setState(
                    {
                        latitude: posicao.coords.latitude,
                        longitude: posicao.coords.longitude,
                        estacao: estacao,
                        data: data.toLocaleTimeString(),
                        icone: icone,
                    }
                );
            },
            (erro) => {
                console.log(erro);
                this.setState({
                    mensagemDeErro: "Tente novamente mais tarde",
                });
            }
        )
    }

    render() {
        console.log(this.state)
        return (
            // responsividade, margem acima
            <div className="container mt-2">
                {/* uma linha, conteúdo centralizado, display é flex */}
                <div className="row justify-content-center">
                    {/* oito colunas das doze disponíveis serão usadas para telas médias em diante
        */}
                    <div className="col-md-8">
                        {/* um cartão Bootstrap */}
                        <div className="card">
                            {/* o corpo do cartão */}
                            <div className="card-body">
                                {/* centraliza verticalmente, margem abaixo */}
                                <div className="d-flex align-items-center border rounded mb-2"
                                    style={{ height: '6rem' }}>
                                    {/* ícone obtido do estado do componente */}
                                    <i className={`fas fa-5x ${this.state.icone}`}></i>
                                    {/* largura 75%, margem no à esquerda (start), fs aumenta a fonte */}
                                    <p className=" w-75 ms-3 text-center fs-1">{this.state.estacao}</p>
                                </div>
                                <div>
                                    <p className="text-center">
                                        {/* renderização condicional */}
                                        {
                                            this.state.latitude ?
                                                `Coordenadas: ${this.state.latitude},
${this.state.longitude}. Data: ${this.state.data}` : this.state.mensagemDeErro
                                                    ? this.state.mensagemDeErro
                                                    : "Clique no botão para saber a sua estação climática"}
                                    </p>

                                </div>
                                {/* botão azul (outline, 100% de largura e margem acima) */}
                                <button onClick={this.obterLocalizacao}
                                    className="btn btn-outline-primary w-100 mt-2">
                                    Qual a minha estação?
                                </button>

                            </div>
                        </div>

                    </div>
                </div>
            </div>
        )
    }

}
const root = createRoot(document.getElementById('root'))
root.render(<App />)