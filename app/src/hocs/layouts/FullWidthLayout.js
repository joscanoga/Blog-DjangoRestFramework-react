import React from 'react'
import { connect } from 'react-redux'
import Footer from '../../components/navigation/footer'
import Navbar from '../../components/navigation/Navbar'
function FullWidthLayout({children}) {
  return (
    <div>
        <Navbar/>
        {children}
        <Footer/>
    </div>
  )
}

const mapStateToProps = (state) => ({
})
export default connect(mapStateToProps,{})(FullWidthLayout)