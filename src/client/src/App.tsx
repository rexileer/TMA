import { useQuery } from "@tanstack/react-query";
import request from "./utils/api";
import { IUser } from "./interface/IUser";
import { init, initData, viewport } from "@telegram-apps/sdk"

init();
viewport.mount();

initData.restore();
viewport.expand();


const App = () => {
  const { data: user , isLoading} = useQuery({
    queryKey: ["user"],
    queryFn: async () => {
      const response = await request("users/get");
      console.log("Ответ от сервера:", response.data); // Добавь лог
      return response.data;
    },
    select: (data: any) => data.user as IUser,
  })

  return( 
    <div className="h-screen flex items-center justify-center text-white text-3xl">
     {isLoading ? (
      <div className="animate-pulse text-3xl">Loading.....</div>
     ) : (
      <div>{user?.name}</div>
     )}
    </div>
  );
};

export default App;