import React from 'react'

export class EstacaoClimatica extends React.Component {
  // Class field for the timer reference — we need to remember the ID that
  // setInterval returns so we can later pass it to clearInterval. Without
  // this, the timer would keep firing forever even after the component dies.
  timer = null

  // Local state: just the displayed time. This is OWNED by this component
  // because only this component needs to know about it — App doesn't care.
  state = {
    data: null
  }

  // ─────────────────────────────────────────────────────────────────────
  // LIFECYCLE METHODS — the whole point of this lesson
  // ─────────────────────────────────────────────────────────────────────

  // Runs ONCE, right after the first render puts this component in the DOM.
  // Perfect place to start a timer, fetch data, subscribe to events, etc.
  componentDidMount() {
    console.log('EstacaoClimatica: componentDidMount')

    // setInterval schedules the arrow function to run every 1000ms (1 second).
    // Each tick updates state, which triggers a re-render, which shows the
    // new time. This is what makes the clock "tick" visually.
    this.timer = setInterval(() => {
      this.setState({ data: new Date().toLocaleTimeString() })
    }, 1000)
  }

  // Runs after EVERY update (any time state or props change and re-render).
  // Watch the console: you'll see this fire once per second along with render,
  // because setState above causes an update every time the clock ticks.
  componentDidUpdate() {
    console.log('EstacaoClimatica: componentDidUpdate')
  }

  // Runs ONCE, right before this component is removed from the DOM.
  // CRITICAL: if you forget to clearInterval here, the timer keeps firing
  // on a component that no longer exists — React will warn you, and you'll
  // leak memory. This is the canonical "cleanup" use case the PDF teaches.
  componentWillUnmount() {
    console.log('EstacaoClimatica: componentWillUnmount')
    clearInterval(this.timer)
  }

  render() {
    console.log('EstacaoClimatica: render')
    return (
      <div className="card">
        <div className="card-body">
          {/* Top row: big season icon + season name, side by side */}
          <div
            className="d-flex align-items-center border rounded mb-2"
            style={{ height: '6rem' }}
          >
            {/* Icon class comes from props — App decides which season icon to show */}
            <i className={`fas fa-5x ${this.props.icone}`}></i>
            <p className="w-75 ms-3 text-center fs-1">
              {this.props.estacao}
            </p>
          </div>

          {/* Middle row: coordinates + live-updating clock */}
          <div>
            <p className="text-center">
              {this.props.latitude
                ? `Coordenadas: ${this.props.latitude}, ${this.props.longitude}. Data: ${this.state.data}`
                : 'Clique no botão para saber a sua estação climática'}
            </p>
          </div>

          {/* Refresh button — note `obterLocalizacao` comes from App via props.
              A child can't directly modify a parent's state, but the parent
              can pass down a function that does it. This is the "lifting state
              up" pattern, illustrated in Figure 2.5.3 of the PDF. */}
          <button
            onClick={this.props.obterLocalizacao}
            className="btn btn-outline-primary w-100 mt-2"
          >
            Qual a minha estação?
          </button>
        </div>
      </div>
    )
  }
}