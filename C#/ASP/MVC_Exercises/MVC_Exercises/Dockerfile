FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["MVC_Exercises/MVC_Exercises.csproj", "MVC_Exercises/"]
RUN dotnet restore "MVC_Exercises/MVC_Exercises.csproj"
COPY . .
WORKDIR "/src/MVC_Exercises"
RUN dotnet build "MVC_Exercises.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "MVC_Exercises.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "MVC_Exercises.dll"]
