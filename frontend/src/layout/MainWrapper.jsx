import { useEffect, useState } from "react";
import { setUser } from "../utils/auth";

const MainWrapper = ({ children }) {
    const [loading, setLoading] = useState(true);

    // useEffect hook to handle side effects after component mounting
    useEffect(async () => {
        const handler = async () =>{
            setLoading(true)
            await setUser
            setLoading(false)
        }
        handler()
    }, [])

    return <>{loading ? null : children}</>

}

export default MainWrapper