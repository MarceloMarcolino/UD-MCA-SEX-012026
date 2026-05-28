 import React from 'react' 
 
const Imagem = ({ pic, imgStyle }) => { 
    return ( 
        <div className={`${imgStyle} flex justify-content-center`}> 
            <img className="border-round" src={pic} alt="Imagem" /> 
        </div> 
    ) 
} 
 
export default Imagem 