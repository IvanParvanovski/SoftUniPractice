FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex4RectangleClass/Ex4RectangleClass.csproj", "Ex4RectangleClass/"]
RUN dotnet restore "Ex4RectangleClass/Ex4RectangleClass.csproj"
COPY . .
WORKDIR "/src/Ex4RectangleClass"
RUN dotnet build "Ex4RectangleClass.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex4RectangleClass.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex4RectangleClass.dll"]
