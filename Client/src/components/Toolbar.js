import React from 'react'
import Navbar from 'react-bootstrap/Navbar'
import bellImage from '../images/bells_big.png'
import '../Palette.css'

function Toolbar(){
    return(
        <Navbar bg="primary" variant='dark' expand="sm" fixed="top">
            <Navbar.Brand>
                <img src={bellImage} width="30" height="30" alt="Bells Icon" />
                Seasonpedia
            </Navbar.Brand>
        </Navbar>
    )
}

export default Toolbar;