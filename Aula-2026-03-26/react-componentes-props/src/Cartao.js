import React from 'react';

const Cartao = (props) => {
    return (
        <div className="card">
            {/* Cabeçalho do cartão */}
            <div className="card-header text-muted">{props.cabecalho}</div>
            {/* Corpo do cartão */}
            <div className="card-body">
                {props.children}
            </div>
        </div>
    );
};

export default Cartao;