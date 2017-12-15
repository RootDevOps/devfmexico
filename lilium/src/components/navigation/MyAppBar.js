import React from 'react';

import {purpleA700} from 'material-ui/styles/colors';

import select from './selectfield';


import PlaceCard from '../places/PlaceCard'



export default class MyAppBar extends React.Component {

state = { listaFlores : []}
changeSelect = (e) => {
  let ciudad = e.target.value;
  var myRequest = 'http://95eae9c0.ngrok.io/api/v1/stores/search/'+ciudad+'/'
       fetch(myRequest)
           .then((response) =>{ return response.json(); })
           .then((resposeJson)=> {
               let flores = [];
               flores = resposeJson.map((datos) => {
                   return datos.cut_flowers;
               });
               console.log(flores)
               this.setState(()=>({listaFlores:flores}));
           }).catch(e => console.log(e));
  console.log(e.target.value)
}

renderCard = (datos) =>{
  return datos.map((flores)=>{
    return <PlaceCard key={datos.id}
                        nombre={flores.name_cutflower}
                        precio={flores.pricesend_cutflower}
                        imagen={flores.image_cutflower}
                        ocultar={()=>this.ocultar(flores.id)}
                        descripcion={flores.descripcion}/>
  });
};

 ocultar = (id) => {
 this.setState(()=>({
    listaFlores : this.state.listaFlores.map( elementos =>{
        return elementos.filter(el => el.id != id);
    } )
  }))
}
  render() {


    const {listaFlores} =this.state;
    return (

        <div className="AppBar" style={{'backgroundColor': purpleA700}}>
      <div className="buscador">
      <div>
        <h1 style={{'color': "white"}}>Buscar</h1>
      </div>
      <div>
       <select onChange={this.changeSelect}>
       <option value='CDMX'> CDMX </option>
       <option value='Mexico'> Mexico</option>
       <option value='Oaxaca'> Oaxaca</option>
       </select>
       </div>
      </div>

         {listaFlores.map(this.renderCard)}
        </div>


    );
  }
}
