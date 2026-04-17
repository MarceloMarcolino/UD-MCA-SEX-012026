import React from 'react'
import ReactDOM from 'react-dom/client'
import { EstacaoClimatica } from './EstacaoClimatica.js'
import Loading from './Loading'

// Creating the React root first so we have access to it inside the class
// (the PDF references `root.unmount()` in the Unmount button demo)
const root = ReactDOM.createRoot(document.getElementById('root'))

class App extends React.Component {
  // This is the "no-constructor" state initialization style the PDF teaches
  // in section 2.4 — less verbose than writing a constructor + super(props)
  state = {
    latitude: null,
    longitude: null,
    estacao: null,
    icone: null,
    mensagemDeErro: null
    // Note: `data` (the time) lives in EstacaoClimatica's own state now,
    // because the timer that updates it every second belongs to that component.
  }

  // componentDidMount runs ONCE, right after the first render.
  // The PDF (section 2.3) uses it to kick off the geolocation request
  // immediately so the user sees their season without clicking anything.
  componentDidMount() {
    this.obterLocalizacao()
  }

  // Arrow function syntax auto-binds `this` — important because we pass
  // this method down as a prop and it will be called from the child.
  obterLocalizacao = () => {
    window.navigator.geolocation.getCurrentPosition(
      (position) => {
        // Success: figure out which season it is based on the month
        const { latitude, longitude } = position.coords
        const { estacao, icone } = this.calcularEstacao(latitude)
        this.setState({
          latitude: latitude.toFixed(6),
          longitude: longitude.toFixed(6),
          estacao,
          icone,
          mensagemDeErro: null
        })
      },
      (err) => {
        // Failure: user blocked location, or it's unavailable
        this.setState({ mensagemDeErro: err.message })
      }
    )
  }

  // Simple helper: determines season from the current month + hemisphere.
  // Southern hemisphere (negative latitude) has seasons flipped vs. northern.
  calcularEstacao = (latitude) => {
    const mes = new Date().getMonth() // 0 = January, 11 = December
    const hemisferioSul = latitude < 0

    let estacao
    if (mes >= 2 && mes <= 4) estacao = hemisferioSul ? 'Outono' : 'Primavera'
    else if (mes >= 5 && mes <= 7) estacao = hemisferioSul ? 'Inverno' : 'Verão'
    else if (mes >= 8 && mes <= 10) estacao = hemisferioSul ? 'Primavera' : 'Outono'
    else estacao = hemisferioSul ? 'Verão' : 'Inverno'

    // Map each season to a Font Awesome icon class
    const icones = {
      'Verão': 'fa-sun',
      'Outono': 'fa-leaf',
      'Inverno': 'fa-snowman',
      'Primavera': 'fa-seedling'
    }
    return { estacao, icone: icones[estacao] }
  }

  render() {
    return (
      <div className="container mt-2">
        <div className="row justify-content-center">
          <div className="col-md-8">
            {
              // This is the 3-way conditional from section 2.8 of the PDF.
              // It decides WHICH component to show based on current state:
              //   1. No latitude AND no error  → user hasn't decided → show spinner
              //   2. Error present             → user blocked access  → show error text
              //   3. Otherwise (have latitude) → show the weather card
              (!this.state.latitude && !this.state.mensagemDeErro) ?
                <Loading mensagem="Por favor, responda à solicitação de localização" />
              : this.state.mensagemDeErro ?
                <p className="border rounded p-2 fs-1 text-center">
                  É preciso dar permissão para acesso à localização.
                  Atualize a página e tente de novo, ajustando a configuração no seu navegador.
                </p>
              :
                <EstacaoClimatica
                  icone={this.state.icone}
                  estacao={this.state.estacao}
                  latitude={this.state.latitude}
                  longitude={this.state.longitude}
                  obterLocalizacao={this.obterLocalizacao}
                />
            }
          </div>
        </div>
      </div>
    )
  }
}

root.render(<App />)