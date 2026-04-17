import React, { Component } from 'react'

export default class Loading extends Component {
  render() {
    return (
      // flex-column stacks the spinner on top of the message vertically.
      // Without flex-column they'd sit side-by-side, which looks cramped.
      <div className="d-flex flex-column justify-content-center align-items-center border rounded p-3">
        <div
          className="spinner-border text-primary"
          style={{ width: '3rem', height: '3rem' }}
        >
          {/* visually-hidden is a Bootstrap class: hides this from sighted
              users but screen readers still announce it. Accessibility matters. */}
          <span className="visually-hidden">Carregando...</span>
        </div>

        {/* The message comes from props — whoever uses <Loading /> gets to
            pick the text. If they don't pass one, defaultProps below fills in. */}
        <p className="text-primary mt-2">{this.props.mensagem}</p>
      </div>
    )
  }
}

// defaultProps lives OUTSIDE the class, attached to the component itself.
// React checks here automatically when a prop isn't provided by the parent.
// This is cleaner than writing `{this.props.mensagem || 'Carregando'}`
// everywhere, and it scales well when you have many optional props.
Loading.defaultProps = {
  mensagem: 'Carregando'
}